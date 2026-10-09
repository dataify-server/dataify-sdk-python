# Dataify Python SDK 更新发布步骤

适用于把当前 `dataify-sdk` 新版本发布到 PyPI。

## 1. 更新版本号

修改两个位置，版本号必须一致：

```text
pyproject.toml
src/dataify_sdk/__init__.py
```

例如本次新增公开方法，建议改为：

```text
1.1.0
```

## 2. 检查代码状态

```powershell
git status --short
```

确认只包含本次要发布的改动。

## 3. 安装开发依赖

```powershell
python -m pip install -e ".[dev]"
```

## 4. 运行测试

```powershell
python -m pytest
python -m compileall src tests
```

测试通过后再继续。

## 5. 安装发布工具

```powershell
python -m pip install --upgrade build twine
```

## 6. 清理旧构建产物

```powershell
Remove-Item -LiteralPath .\dist -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath .\build -Recurse -Force -ErrorAction SilentlyContinue
```

## 7. 构建新版本

```powershell
python -m build
```

构建后检查 `dist/` 下是否生成：

```text
*.tar.gz
*.whl
```

## 8. 检查发布包

```powershell
python -m twine check --strict dist/*
```

必须通过。

## 9. 先发到 TestPyPI

```powershell
python -m twine upload --repository testpypi dist/*
```

登录时：

```text
username: __token__
password: TestPyPI token
```

如果看到 `WARNING This environment is not supported for trusted publishing`，本机发布时可以忽略，继续用上面的 token 登录即可。

如果返回 `403 Forbidden`，先执行：

```powershell
python -m twine upload --repository testpypi --verbose dist/*
```

常见原因：

- 用了正式 PyPI token；TestPyPI 必须用 TestPyPI 单独创建的 token。
- token 对应账号不是 `dataify-sdk` 在 TestPyPI 上的 owner/maintainer。
- 项目级 token 只能上传已有项目；首次创建项目建议用 TestPyPI 账号级 token。
- TestPyPI 账号邮箱未验证。
- 版本号或文件已上传过，换一个新版本号后重新构建。

## 10. 从 TestPyPI 安装验证

```powershell
python -m venv .venv-testpypi-check
.\.venv-testpypi-check\Scripts\python -m pip install --upgrade pip
.\.venv-testpypi-check\Scripts\python -m pip install --index-url https://test.pypi.org/simple/ --no-deps dataify-sdk==<版本号>
.\.venv-testpypi-check\Scripts\python -c "import dataify_sdk; print(dataify_sdk.__version__)"
```

确认输出版本号正确。

## 11. 发布到正式 PyPI

```powershell
python -m twine upload dist/*
```

登录时：

```text
username: __token__
password: PyPI token
```

如果看到 `WARNING This environment is not supported for trusted publishing`，本机发布时可以忽略，继续用上面的 token 登录即可。

## 12. 从正式 PyPI 安装验证

```powershell
python -m venv .venv-pypi-check
.\.venv-pypi-check\Scripts\python -m pip install --upgrade pip
.\.venv-pypi-check\Scripts\python -m pip install --no-cache-dir dataify-sdk==<版本号>
.\.venv-pypi-check\Scripts\python -c "import dataify_sdk; print(dataify_sdk.__version__)"
```

确认输出版本号正确。

## 13. 打 Git Tag

```powershell
git tag v<版本号>
git push origin v<版本号>
```

## 注意

- PyPI 已发布的同版本不能覆盖上传。
- token 不要写进代码、README 或提交记录。
- 如果发布后发现问题，直接修复后发下一个版本。
