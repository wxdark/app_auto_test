from page.page_address_list import PageAddressList
from page.page_category import PageCategory
from page.page_edit_address import PageEditAddress
from page.page_goods_detail import PageGoodsDetail
from page.page_goods_list import PageGoodsList
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_register import PageRegister
from page.page_setting import PageSetting
from page.page_shop_cart import PageShopCart
from page.page_updtae import PageUpdate
from page.page_user_center import PageUserCenter
from page.page_vip import PageVip


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return PageHome(self.driver)

    @property
    def register(self):
        return PageRegister(self.driver)

    @property
    def login(self):
        return PageLogin(self.driver)

    @property
    def user_center(self):
        return PageUserCenter(self.driver)

    @property
    def update(self):
        return PageUpdate(self.driver)

    @property
    def setting(self):
        return PageSetting(self.driver)

    @property
    def vip(self):
        return PageVip(self.driver)

    @property
    def address_list(self):
        return PageAddressList(self.driver)

    @property
    def edit_address(self):
        return PageEditAddress(self.driver)

    @property
    def category(self):
        return PageCategory(self.driver)

    @property
    def goods_list(self):
        return PageGoodsList(self.driver)

    @property
    def goods_detail(self):
        return PageGoodsDetail(self.driver)

    @property
    def shop_cart(self):
        return PageShopCart(self.driver)


