import base64
import os
from pathlib import Path
from urllib.parse import quote

import pytest
import pytest_html
from playwright.sync_api import sync_playwright

from config import BASE_URL


@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = None

    try:
        browser = playwright.chromium.launch(
            args=["--start-maximized"],
            headless=False,
        )
        yield browser
    finally:
        try:
            if browser is not None:
                browser.close()
        finally:
            playwright.stop()


@pytest.fixture
def page(request, browser):
    recordings_dir = Path("recordings")
    recordings_dir.mkdir(exist_ok=True)

    context = browser.new_context(
        ignore_https_errors=True,
        no_viewport=True,
        record_video_dir=str(recordings_dir),
    )
    page = context.new_page()
    video = page.video

    try:
        page.goto(BASE_URL)
        page.wait_for_load_state("load")
        yield page
    finally:
        context.close()
        if video is not None:
            request.node._video_path = video.path()


def _report_content(item, path):
    if item.config.getoption("self_contained_html", default=False):
        return base64.b64encode(Path(path).read_bytes()).decode("ascii")

    html_path = getattr(item.config.option, "htmlpath", None)
    if html_path:
        report_path = Path(
            item.config.invocation_params.dir,
            os.path.expandvars(str(html_path)),
        ).expanduser()
        try:
            relative_path = os.path.relpath(path, report_path.parent)
        except ValueError:
            return Path(path).resolve().as_uri()
        return quote(Path(relative_path).as_posix())

    return Path(path).resolve().as_uri()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            screenshots_dir = Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            file_name = screenshots_dir / f"{item.name}.png"
            page.screenshot(path=str(file_name))
            extras.append(
                pytest_html.extras.image(
                    _report_content(item, file_name),
                    name="Screenshot",
                )
            )

    if report.when == "teardown":
        video_path = getattr(item, "_video_path", None)
        if video_path:
            extras.append(
                pytest_html.extras.video(
                    _report_content(item, video_path),
                    name="Recording",
                    mime_type="video/webm",
                    extension="webm",
                )
            )

    report.extras = extras
