from Common.Baseui import baseUI
from time import sleep
from selenium.webdriver.support.select import Select

class Test_mall():

    def test_login(self,driver):
        # 使用baseUI
        base = baseUI(driver)
        # 打开登录界面
        driver.get('http://192.168.60.132/#/login')
        # 输入用户名
        base.send_keys('输入用户名','''//input[@name="username"]''','admin')
        # 输入密码
        base.send_keys('输入密码','''//input[@name="password"]''','123456')
        # 点击登录
        base.click('点击登录','''//span[contains(text(),'登录')]''')
        sleep(3)
        assert '首页' in driver.page_source

    def test_fahuo(self,driver):
        # 使用baseUI
        base = baseUI(driver)
        # # 打开界面
        # driver.get('http://192.168.60.132/#/oms/order')
        # # 点击登录
        # base.click('点击登录', '''//span[contains(text(),'登录')]''')
        # 点击订单
        base.click('点击订单','''//span[text()='订单']''')
        sleep(1)
        # 点击订单列表
        base.click('点击订单列表','''(//span[text()='订单']/../following-sibling::ul//span[text()='订单列表']''')
        # 点击订单状态
        base.click('点击订单状态','''//label[text()='订单状态：']/..//input[@placeholder="全部"]''')
        # 点击待发货
        base.click('点击待发货','''//span[text() = '待发货']''' )
        sleep(1)
        # 点击查询搜索
        base.click('点击查询搜索','''//span[contains(text(),'查询搜索')]''')
        sleep(1)
        # 点击订单发货
        base.click('点击订单发货','''(//span[contains(text(),'订单发货')])[1]''')
        # 点击快递公司
        base.click('点击快递公司','''//input[ @ placeholder = "请选择物流公司"]''' )
        # 选择圆通快递
        base.click('选择圆通快递','''// span[text() = '圆通快递']''')
        sleep(1)
        #填写单号
        base.send_keys('填写单号','''(//input[@class="el-input__inner"])[2]''','123456789')
        # 点击确定
        base.click('点击确定','''(//span[contains(text(),'确定')])[1]''')
        sleep(1)
        # 点击弹框确定
        base.click('点击弹框确定','''(//span[contains(text(),'确定')])[2]''')
        sleep(2)
        #获取提示文本
        text = base.get_text('获取提示文本', '''//div[@aria-label="提示"]/following-sibling::div//p''')
        assert text in driver.page_source


    def test_tuohuo(self,driver):
        # 使用baseUI
        base = baseUI(driver)
        # # 打开界面
        driver.get('http://192.168.60.132/#/oms/order')
        # # 点击登录
        base.click('点击登录', '''//span[contains(text(),'登录')]''')
        # 点击订单
        base.click('点击订单', '''//span[text()='订单']''')
        # 点击退货申请处理(//ul[@role="menu"])[2]/a[3]//span
        base.click('点击退货申请处理','''(//ul[@role="menu"])[2]/a[3]//span''')
        # 点击处理状态//label[text()='处理状态：']/..//input
        base.click('点击处理状态','''//label[text()='处理状态：']/..//input''')
        # 点击待处理(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]//span[text()='待处理']
        base.click('点击待处理','''(//ul[@class="el-scrollbar__view el-select-dropdown__list"])[3]//span[text()='待处理']''')
        # 点击查询搜索//span[text()='筛选搜索']/..//span[contains(text(),'查询搜索')]
        base.click('点击查询搜索','''//span[text()='筛选搜索']/..//span[contains(text(),'查询搜索')]''')
        # 点击查看详情//tbody/tr[1]/td[8]//span
        base.click('点击查看详情','''//tbody/tr[1]/td[8]//span''')
        #滚动窗口至最下方
        base.scroll_screen('滚动窗口至最下方')
        sleep(1)
        # 获取金额文本//div[text()='订单金额']/following-sibling::div
        text = base.get_text('获取金额文本', '''//div[text()='订单金额']/following-sibling::div''')
        text1=str(text)
        text=text1[1:]
        # 填写退款金额(退款金额=订单金额)//div[contains(text(),'确认退款金额')]/..//input
        base.send_keys('填写退款金额(退款金额=订单金额)','''//div[contains(text(),'确认退款金额')]/..//input''',text)
        sleep(2)
        # 点击确认退货(//button[@class="el-button el-button--primary el-button--small"])[1]//span
        base.click('点击确认退货','''(//button[@class="el-button el-button--primary el-button--small"])[1]//span''')
        # 点击确认//div[@role="dialog"]//span[contains(text(),'确定')]
        base.click('点击确认','''//div[@role="dialog"]//span[contains(text(),'确定')]''')
        # 获取文本//div[@role="alert"]//p
        get_text = base.get_text('获取文本', '''//div[@role="dialog"]/following-sibling::div//p''')
        # 做断言
        assert '操作成功' in get_text
        sleep(1)


# 字符串:find/split/replace(查找,切割,替换)
a='adf,fhggfhdad,qerrtadf,24ds'
#find 查找
print(a.find("qerrtadf"))
#split 切割
print(a.split(','))
#replace 替换
print(a.replace('a','1'))