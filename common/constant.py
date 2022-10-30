import os

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conf_test_dir = os.path.join(root_dir, 'config', 'conf_test.cfg')
print(conf_test_dir)
conf_uat_dir = os.path.join(root_dir, 'config', 'conf_uat.cfg')

conf_prod_dir = os.path.join(root_dir, 'config', 'conf_prod.cfg')

globe_conf_dir = os.path.join(root_dir, 'config', 'globe_conf.cfg')

log_dir = os.path.join(root_dir, 'log')

report_dir = os.path.join(root_dir, 'report')

data_dir = os.path.join(root_dir, "data")

dev_desired_caps_dir = os.path.join(root_dir, 'data', 'desired_caps.yaml')

dev_login_dir = os.path.join(root_dir, "data", "login.yaml")




