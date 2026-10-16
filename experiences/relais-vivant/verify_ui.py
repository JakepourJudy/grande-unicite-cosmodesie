"""Optional browser check: pip install playwright; playwright install chromium.

Run locally, or pass --url for the published page. An already installed Chromium
browser can be selected with --browser-executable. Uses an isolated headless context.
"""
import argparse
import json
from pathlib import Path
from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default=Path(__file__).with_name('demo.html').as_uri())
    parser.add_argument('--browser-executable')
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    errors = []
    with sync_playwright() as p:
        options = {'headless': True}
        if args.browser_executable:
            options['executable_path'] = args.browser_executable
        browser = p.chromium.launch(**options)
        page = browser.new_page(viewport={'width': 1280, 'height': 1100})
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.goto(args.url)
        for preset, expected in [('base', '50 / 64'), ('late', '24 / 64'),
                                 ('cut', '0 / 64'), ('short', '0 / 16'),
                                 ('fragile', '0 / 64')]:
            page.select_option('#preset', preset)
            assert page.locator('#count').inner_text() == expected, preset
        page.select_option('#preset', 'base')
        page.locator('.cell').filter(has_text='4,4').first.click()
        page.locator('#actions button').first.click()
        assert page.locator('#trace li').count() == 1
        page.click('#reset')
        assert page.locator('#trace li').count() == 0
        if args.screenshots:
            args.screenshots.mkdir(parents=True, exist_ok=True)
            page.screenshot(path=str(args.screenshots/'desktop.png'), full_page=True)
        page.set_viewport_size({'width': 390, 'height': 844})
        assert not page.evaluate('document.documentElement.scrollWidth > innerWidth')
        if args.screenshots:
            page.screenshot(path=str(args.screenshots/'mobile.png'), full_page=True)
        assert not errors, errors
        print(json.dumps({'status': 'PASS', 'presets': 5, 'action_and_reset': True,
                          'mobile_no_horizontal_overflow': True, 'page_errors': errors}))
        browser.close()


if __name__ == '__main__':
    main()
