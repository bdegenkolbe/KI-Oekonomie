const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
(async () => {
  const [src, pdf, scheme, shot] = process.argv.slice(2);
  const html = '<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">' + fs.readFileSync(src, 'utf8').replace('<main', '</head><body><main') + '</body></html>';
  const tmp = require('os').tmpdir() + '/haftungswende-voll.html'; fs.writeFileSync(tmp, html);
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined, args: ['--ignore-certificate-errors-spki-list'] });
  const p = await b.newPage({ viewport: { width: 1100, height: 1400 }, colorScheme: scheme || 'light' });
  const { execFileSync } = require('child_process');
  await p.route(/fonts\.(googleapis|gstatic)\.com/, async route => {
    const url = route.request().url();
    const body = execFileSync('curl', ['-sS', '--cacert', '/root/.ccr/ca-bundle.crt', '-A', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0 Safari/537.36', url]);
    const ct = url.includes('googleapis') ? 'text/css' : 'font/woff2';
    await route.fulfill({ status: 200, body, headers: { 'content-type': ct, 'access-control-allow-origin': '*' } });
  });

  await p.goto('file://' + tmp, { waitUntil: 'networkidle', timeout: 60000 }).catch(e => console.log('goto', e.message));
  await p.evaluate(() => document.fonts.ready);
  console.log('fonts', await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family).join(',')));
  if (shot) { await p.screenshot({ path: shot, fullPage: true }); }
  if (pdf) {
    await p.emulateMedia({ media: 'print', colorScheme: 'light' });
    await p.pdf({ path: pdf, format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: '<div style="width:100%;font:8px Arial,sans-serif;color:#627089;padding:0 14mm;display:flex;justify-content:space-between"><span>Die Haftungswende · HIGL-Verbund · Fassung 2.0 · Stand 26.09.2026</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>' });
  }
  await b.close();
})();
