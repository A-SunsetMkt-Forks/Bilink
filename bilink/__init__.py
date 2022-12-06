from bilink.utils.login import BiliLogin as Login
from asyncio import run
from bilink.utils import listening
from bilink.utils.cookies import Cookies


async def running():
    """自动判断登录方式"""
    cookies = Cookies()
    check = await cookies.check()
    if check:
        cookies_ = await cookies.load_cookie()
        try:
            listening.run(cookies_)
        except Exception as e:
            str(e)
            await cookies.delete()
    else:
        cookies_ = await cookies.get_cookie()
        await cookies.save_cookie(cookies_)
        listening.run(cookies_)


if __name__ == '__main__':
    run(running())
