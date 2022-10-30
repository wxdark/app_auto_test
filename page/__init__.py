"""百年奥莱项目参数配置"""
from selenium.webdriver.common.by import By

from appium.webdriver.common.mobileby import MobileBy

# 首页参数配置

home_close_update = By.ID, "com.yunmall.lc:id/img_close"  # 版本更新弹窗按钮

home_click_user = By.ID, "com.yunmall.lc:id/tab_me"  # 首页我的按钮

home_category = By.ID, "com.yunmall.lc:id/tab_category"  # 首页分类按钮

home_shop_cart = By.ID, "com.yunmall.lc:id/tab_shopping_cart"  # 首页购物车按钮

# 商品分类列表页
category_goods_list = By.ID, "com.yunmall.lc:id/iv_img"  # 分类商品列表

# 商品列表
goods_list = By.ID, "com.yunmall.lc:id/iv_element_1"  # 商品
# 商品详情
goods_detail_add_shopcart = By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"  # 加入购物车按钮

goods_detail_confirm_btn = By.ID, "com.yunmall.lc:id/select_detail_sure_btn"  # 点击确认按钮
# 注册页参数配置
register_go_login = By.XPATH, "//*[@text='已有账号，去登录']"  # 注册页已有账号，去登录

# 登录页参数配置
login_input_account = By.ID, "com.yunmall.lc:id/logon_account_textview"  # 输入用户名

login_input_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"  # 输入密码框

login_btn = By.ID, "com.yunmall.lc:id/logon_button"  # 登录按钮

# 个人中心参数配置
user_center_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"  # 用户昵称

user_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"  # 设置按钮

user_join_vip = By.XPATH, "//*[@text='加入超级VIP']"

# 设置中心参数配置
setting_about = By.ID, "com.yunmall.lc:id/setting_about_yunmall"  # 关于百年奥莱

setting_clear_cache = By.ID, "com.yunmall.lc:id/setting_clear_cache"  # 清除缓存

setting_address = By.ID, "com.yunmall.lc:id/setting_address_manage"  # 地址管理按钮

setting_quit = By.ID, "com.yunmall.lc:id/setting_logout"  # 退出登录按钮

setting_quit_enter = By.ID, "com.yunmall.lc:id/ymdialog_right_button"  # 确认退出登录按钮

# 版本更新页参数配置
about_update = By.XPATH, "//*[@text = '版本更新']"

# 加入vip页面参数配置
vip_invitation_code = By.XPATH, "//input[@type='tel']"

vip_become = By.XPATH, "//*[@value='立即成为会员']"

# 地址管理页面参数配置
address_add_btn = By.ID, "com.yunmall.lc:id/address_add_new_btn"  # 新增地址

address_receipt_name = By.ID, "com.yunmall.lc:id/receipt_name"  # 联系人、手机号文本信息

address_is_default = By.ID, "com.yunmall.lc:id/address_is_default"  # 默认地址图标

address_edit_btn = By.XPATH, "//*[@text='编辑']"  # 编辑按钮

address_delete_btn = By.XPATH, "//*[@text='删除']"  # 删除按钮

address_confirm_btn = By.XPATH, "//*[@text='确认']"  # 点击删除后确认按钮

# 编辑地址页参数配置
edit_add_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"  # 新增收件人

edit_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"  # 新增手机号

edit_add_detail_addr_info = By.ID, "com.yunmall.lc:id/address_detail_addr_info"  # 新增详细地址

edit_add_post_code = By.ID, "com.yunmall.lc:id/address_post_code"  # 邮编

edit_add_address_default = By.ID, "com.yunmall.lc:id/address_default"  # 设为默认地址

edit_add_address_province = By.ID, "com.yunmall.lc:id/address_province"  # 选择地区

edit_add_save_btn = By.ID, "com.yunmall.lc:id/button_send"  # 保存按钮

edit_add_area_title = By.ID, "com.yunmall.lc:id/area_title"  # 省市区

# 购物车页参数配置
shop_cart_selection_button = By.ID, "com.yunmall.lc:id/iv_select_all"  # 购物车全选按钮

shop_cart_total_price = By.ID, "com.yunmall.lc:id/tv_count_money"  # 购物车商品总价

shop_cart_price = By.ID, "com.yunmall.lc:id/tv_price"  # 购物车商品单价

shop_cart_edit_btn = By.XPATH, "//*[@text='编辑']"  # 购物车编辑按钮

shop_cart_complete_btn = By.XPATH, "//*[@text='完成']"  # 购物车完成按钮

shop_cart_add_count = By.ID, "com.yunmall.lc:id/iv_add"  # 添加商品数量

shop_cart_delete_btn = By.ID, "com.yunmall.lc:id/tv_del_all"  # 删除按钮

shop_cart_affirm = By.XPATH, "//*[@text = '确认']"  # 删除确认

shop_cart_is_empty = By.XPATH, "//*[contains(@text, '购物车还是空的')]"

