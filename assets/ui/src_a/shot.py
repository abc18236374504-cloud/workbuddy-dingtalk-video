import pathlib
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).parent
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    for f in sorted((R/'src').glob('*.html')):
        pg.goto(f.as_uri()); pg.wait_for_timeout(400); pg.screenshot(path=str(R/'out'/(f.stem+'.png')))
    b.close()
