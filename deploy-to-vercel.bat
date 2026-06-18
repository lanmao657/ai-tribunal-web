@echo off
chcp 65001 >nul
echo ========================================
echo   《AI法庭》Vercel 部署脚本
echo ========================================
echo.

cd /d "e:\2026-项目\galgame\AIFT-1.0-dists\AIFT-1.0-web"

echo [1/4] 检查 Vercel CLI...
where vercel >nul 2>&1
if errorlevel 1 (
    echo 正在安装 Vercel CLI...
    call npm install -g vercel
)

echo.
echo [2/4] 登录 Vercel...
echo 如果浏览器自动打开，请完成登录验证。
echo 如果没有自动打开，请访问 CLI 输出的链接。
echo.
vercel login

echo.
echo [3/4] 部署预览版本...
vercel --yes

echo.
echo [4/4] 部署正式版本...
vercel --prod --yes

echo.
echo ========================================
echo   部署完成！
echo   请查看上方输出的网址
echo ========================================
pause
