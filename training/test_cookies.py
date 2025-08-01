"""
Test work with cookies in Selenium.
Command: pytest training\test_cookies.py
"""

import time

from selenium.webdriver.common.by import By

COOKIES = [{'name': 'KXIYO4xMrWh', 'value': 'ibyAZPfXAsPqptPaNyL'},
           {'name': '0OIJ4G4ZLzK', 'value': 'kJcPzQu5Jr8ELK'},
           {'name': 'O1C4sd3RK5udnZ6P', 'value': '4mYYxbfgnIvuip2ry58EQ'},
           {'name': 'AUZgaLJ4Y', 'value': 'FLSZvYrkf1E57YMUkdD'},
           {'name': '9PWJc0VXVtnXNcS5Tf', 'value': 'YQ2G4RayBoXSEqEgA3oXRN3FAvAMT'},
           {'name': 'pN2x6MDb', 'value': 'htbtD59XD3vCemHRCe9iUxV1smvXAIk5XOwuHnnmMB0'},
           {'name': 'AsqpQd', 'value': 'uNFFRiqeRrj25MwJajG4AxeKvCxKbHUSbbvzb3C'},
           {'name': '73PVEdwTk0txDp4L', 'value': 'DTniz3Fwj110H24dfZfd5JqqfEtN'},
           {'name': 'jZ1MwGy5z0L8ZW00U', 'value': 'sspfahNvfeo3zHWAIW0jdp2A9LyDbIm0'},
           {'name': 'aLRosjpBhYrZ0J69a', 'value': 'zcoXWv5L9Pz5kwGeyP5jlAQ'},
           {'name': '9LPCTyKTNmvBcnZ', 'value': 'GWBjw1Gosk4IKxuh5J2eu0ikgowOaZwP8FOm1ekKeQIxJDIXBy'},
           {'name': 'psH0h', 'value': 'wNAUmVlQwG6VK5TvDfryipzWeLXX46WDbXUd8yGrhrA3Hnc'},
           {'name': 'BULl3P', 'value': 'wefA0ljyA82kYpV1OoOixtAIp6xjmiQlS9SLeN'},
           {'name': '3bIJVJCylqgshRC9r1dH', 'value': '6Y6EZE5dttgx7rKzP881nAhRPE'},
           {'name': 'dBDhCzi6VO0', 'value': 'LKMcpZ6bEJy5IY352OMViznSP5OMqS9IgZB0YMv'},
           {'name': '6SGnnuoZ7v', 'value': '6asdYiIPBsMEdO0mQ9Jlq0mSMbJjfg'},
           {'name': '4dfAVZ1qZwijwYMUj', 'value': '3TOxOPelSdN6cK273'},
           {'name': 'RMOPZQILwFr3o637M', 'value': 'RZoaTFTdytqxB6sZhO4ebrhWlxjhMoQn8ZiObpdcGgH'},
           {'name': '08cQ7E3qHOOMk4uy1fLz', 'value': 'YfYkz9boRjDHLTahMuZcAJPzbjwTlRt1iNZzGl'},
           {'name': 'YT1NKf55egy', 'value': '3MSmfnklFY5TzvM8np4guMsJYtmdHmbyHiz3Vp6Rtk7r4GWhC'},
           {'name': 'cTKnm0a3H2euL46Ibi', 'value': 'HCZ0KYkidXfFowGinPuWG19cT79gEJC'},
           {'name': 'mvAz0P7Igjs2JY', 'value': '8O67zvSDHJx'},
           {'name': 'TzWXbWMvDBcKTo', 'value': 'dzwNYZCg4jpxKtpCeumwq0DO2KtGWLIHpQLOrzmGbXMC8G'},
           {'name': '1BMgyMHkzUemIEr', 'value': '08Sd1v8kQi6eB1FTs9qfjDkJ9UfKCLOFGtDgbOlu9v9iiuu'},
           {'name': 'Jig5voy', 'value': 'Pi4OA6hY21TeHlHyPMaMFHgY0BZRcQ9V0nXg'},
           {'name': '10wa7lhCoJXIzEYW5kQ', 'value': 'BFp4YeKWKVKXHTOesJLleaAelwYwPz51C95IYzd'},
           {'name': 'BqXt5D', 'value': 'n99ZSFFhseCs7aVjU31pYSJxqMgFYGfreFZl9ixb2NNHRBp'},
           {'name': 'GJunU5e1BEvfd', 'value': 'y5YFJ3hF9hG45G86MD9W9nRk61JMsh8rsmbFFrDoeJVUfyBvZ'},
           {'name': 'itFJBn79wksvZ15lc2', 'value': 'nXpdqpt0Po84uOuSU'},
           {'name': 'O5Q70eOB5ivJt5DZ', 'value': 'AZRr2ATREeF9HQR2opgF'},
           {'name': '6jBEUxI0a7x790m', 'value': 'comi8Mx5ig95NAiSO8'},
           {'name': 'KpVF7aIkav32LuqIDI', 'value': 'ik4furgLieyUawgJpttvHxWoXm2zO19'},
           {'name': 'OTRFyN', 'value': 'vlzV7Z97sWcJStZgDJiRjzIf'},
           {'name': 'hKLzMbgdIlUTAMYSEo', 'value': 'Tq2l0QJ3ekwxY3uaC8n2ln1nDMWhltFQm2TNaBefAAzk'},
           {'name': 'GJKNrAvRn', 'value': 'dByJXuSsAIz3Rnqa9BvU11okpnSydEZnkaqMQu9RoE'},
           {'name': 'AowB8Q3t74JHmXTGc1', 'value': '02JklRAtbsNNe'},
           {'name': 'xPpvKmo03bGBYrmqw', 'value': '7bf4FgaLKoj6YvGq4huLT5r9eCflo70QhI9gAPkMIuj4Bg'},
           {'name': '8UqFFBP3Dm0s6XM', 'value': 'kSZJPw6oTBwqG94q'},
           {'name': 'WeeXL7bKNWIZZkgX', 'value': 'ap3DPbBYqlfEOZ6'},
           {'name': 'fhdSevpxKUzledgGtbL4', 'value': 'v5I4A3PFOlN9zWPDkedlC2eLbMZ5cn3cf8'},
           {'name': '3H6lO', 'value': 'jxc9994fPQBKpnyr8aZBDZlMAolnxXh'},
           {'name': 'QVen8QnA1648g4Dm9p', 'value': 'RXNYpaUTJlD4xVIOm'},
           {'name': '3PxMnD9w', 'value': 'JC74xNLEc5ujZge7OmXj5EWk3hwdm4OH8FgF60D6pFl'},
           {'name': 'o8yY57CZSN', 'value': 'afO10rX663gaVttfSxeE70Gd22JKxwJAli7EhEdzkxxME'},
           {'name': 'UpAdf46rvxXW', 'value': 'Ft2FEQV71gLnG'},
           {'name': 'WRrpVIAkMKiZVxHt299', 'value': 'FC53hjqCGooNgV'},
           {'name': 'XHViH149aRl5', 'value': 'YbozZeoGCt3gO1kRMoLExcfCotBz'},
           {'name': 'yjNLzeR4k', 'value': 'Chd2mmuK7nxuVTi'},
           {'name': '5M4RGm', 'value': 'tj3HWN5mVpz9zgIie2ac2KHKIeABaou'},
           {'name': 'CcxIZZYgojDZpHnO9zJl', 'value': 'xLiql8yXUxULBG9w2snaMLI4FjSyX'},
           {'name': 'NScrEjcTmwo639PQqki', 'value': 'eOSFemtdjyphiPubTAzTICUhgw92By'},
           {'name': '9b5OpL5NrCpmtsE', 'value': 'VKdEIeX5ZNTghD6sq3qyjBHJaUuXfpQ7YnYb'},
           {'name': 'uyBoiSTHTtxV8Wszttb', 'value': 'SHEEfVcj1jNv3V1oqeT2wfEbWKZ0uJ2ljwv'},
           {'name': 'qR6AeEoEbQb1GYRj', 'value': 'mA66a177y8e6Nm7BlKBvpcUrM3fm6y4K'},
           {'name': 'l0Y9gn8MNtC', 'value': 'M1L2OUmAisn1c6DNB9mJfTHRM9V3HuXUAEGG8Zx'},
           {'name': 'L8m4GeWyECR', 'value': 'QuFfnWXebyrwwqXfVvAN2dbSisST8IgGyLggrVzTjaCeQ'},
           {'name': 'GxJSMQh9aZjFdhgjaAj', 'value': 'phOonlKiMt0xLDtvoB52TbATS1Ggm4Pv5lztk5vTNkXVqp'},
           {'name': 'GRE1eZ8D1bb', 'value': 'llpIP76V4S978YmQcfW'},
           {'name': 'dooT1cyS41bIWEB9c', 'value': 'ORu004k9aFl9FdS77Iz'},
           {'name': 'csjauyxnCpBySvkXTDzS', 'value': 'SJKqcIqWDbUJbxnHfD8jNJzYKb3Yp3TPIRDIpxCNB'},
           {'name': 'Y6CgAqWN8', 'value': 'qu0g6xEm0iJeTKM8NfOZUxP0XQaCtUfiTWHtQJ5soU5cpZ'},
           {'name': 'xxtL44KLbN60b5q', 'value': 'RSNFhhicL7pWpo3gvE3tJbHaIjU'},
           {'name': 'KcvqC30', 'value': '58IlGI646RMaGMYtL5XYqxFq8UaMwjPDNFNApAuDpUI9tMoM4t'},
           {'name': 'y761v6wZDo3V7O', 'value': '3i9iZjnZXdHlJxDz7ZrkPthYdI3PowS5yRomV0v8fR9WVco4'},
           {'name': 'Ixr7AetyC', 'value': 'lYRaNZAnoNHc9UZIoXI9E'},
           {'name': 'QIvvsr04T0JGVJE', 'value': 'tr6fE8moJI897w967QTmKojC730GdkKTUonevQbYsHQ71mi'},
           {'name': 'CBTq9zQjJx', 'value': 'z7BuIeFufYeZysVnrglrDJk8KW8UBWYt62'},
           {'name': '2ALhFQM7svECfgsSaiTa', 'value': 'VGMsulQVoobUe4m6w8dZGej8jFzSES3hzl9OG2csqpl'},
           {'name': '7VQixJTzu2H', 'value': 'jPnLpldHTFNgPCH1RUlmRQx7N58P7CQHajLYvGxho'},
           {'name': 'KdmUSh1SJH6M9', 'value': 'HPKIgmOBqq6Ln6QSPKedXuFpOoWhrOUzCxRMlcoJ2Gd0S7Hd'},
           {'name': 't6B9gl6QeGEDl1LW', 'value': 'kGs0hk4Pmeb83dBbuHTSzIVNcY0G4iucq73lkCMwt6Akv4w'},
           {'name': 'gcjmy3', 'value': 'QtB6duKOGc7eNc9MFwiOOaikXCYQg6dO4m66sJJxkRebKIKiR'},
           {'name': '2oBZU9j', 'value': '2U80qbFDpRElKTshedtaZ42OzYG48OQckEt2Zy9D7T'},
           {'name': 'g2tyy8erqS4E5pdSynCB', 'value': 'VN5zSYJpNHQC14FVl'},
           {'name': 'lLhLcbED3XAgAPaMp', 'value': 'tBUVWsfSNg0Iv4TLPAmBRm2m2nrWh'},
           {'name': 'iUfgKa7OX', 'value': 'GtyGoiA00RNiTgqvbXs78khbzQ7d0rh5xTk1aZK'},
           {'name': 'WQGGXKzZXvRXLC0', 'value': 'itGXA2mVtchzcqstP39BvfBvwh'},
           {'name': 'p37sYwX5mgtwXJl3yFBL', 'value': 'h20iY8XooVE'},
           {'name': 'tubsOLf', 'value': 'YGlaF0EEJrT1c5Z2HBAWnc1Q3an3Ob'},
           {'name': 'mg1Pr2NJJEnw2UkGFg', 'value': 'L48wovkYz32wa16iiswcgbA6JmyVoysUqjfm4i7'},
           {'name': 'V55E3ui8KHXybSDSSnoc', 'value': '7rhA8PSMZFy1aC8CQXbitOxY0qdUkDOUWijijIvlHhtB0q1'},
           {'name': 'AcWBQQy', 'value': 'zl1GXRHA3neBLCN8'},
           {'name': 'PtvgV4eJ21CrPE3xeH9', 'value': '1tU9KvLdq2uRNRKtA'},
           {'name': 'XjuSocgLwoMvFo8a', 'value': 'pvmx5A97Sad0U6d6i'},
           {'name': 'mMpdmPLcZEAZDzNyA8a2', 'value': 'WG6CrZ3zXfxN84hJXUKJq0ZroYditsADYplxwhkgXkUcZ'},
           {'name': 'tojhHp0ZlGrZ8Y3', 'value': 'fqpJvGkfQRT7ytNTU5KPum150MmcVR1nja0QIQRVEOPiNvT7Pg'},
           {'name': 'LDHgCR5PNoqYdffU5', 'value': '7a0tCBgGzylPTGUStOuNXORrRWwy03Upm2CvJX'},
           {'name': 'F4xcvPzuYYAvDrvDi', 'value': 'zQEpxlKpKprtwFbJyx0XYxFrlc8XP2RhRG'},
           {'name': 'fmnoi', 'value': 'yB9333KC4bP4SHUF90Kj7OC9QXz22WAZ3xtZxLi9'},
           {'name': 'TbGdmTkjcC52T7q', 'value': '2HCejTOfB98e30JMj3Pz9Ok9xLz5Y9lkaJaHoRF2vA5xq0i'},
           {'name': 'tg3vMrNIZHs', 'value': '2XRV99ShR8yc0bCe0QOuC9xd0A'},
           {'name': '8FaJo5TVO7TmoOI', 'value': 'bGYulAOS3ARzN3Rsyx9JJzu'},
           {'name': 'YLBwBAUCJ05p5fx2', 'value': 'Z8lGSb7AnZKVwlIqKgRIafpIfTVufj'},
           {'name': 'fpZCwfH', 'value': 'cqo4KOj8LSagd6VUhBrq6RJtUquwK7mJaDQsQb'},
           {'name': 'zjUiv081bH', 'value': 'LSJtgc56ylEJGMd1AhE9QcXudC8g'},
           {'name': 'yiWR1RtAnWH71I1', 'value': 'ruskXwdCQOfbfIgtKcetVb'},
           {'name': 'KMKvYURaBlIEmtyX', 'value': 'NFIzhI600J5QYN'},
           {'name': 'hbFS4sDwQh', 'value': 's4zWhushscPPDDFqT5tzPJqix0HMjjG'},
           {'name': 'b9wAAVSyw4V2LQ', 'value': 'SDkldbPnf6NjLZSxWZV7CpCW'},
           {'name': 'jFhFn0wPFRG', 'value': 'RYqOrD21ZN7aUeBXqISZ2afocnvvwd6hw3BXUj1wEm0mUO'}]


def test_get_one_cookie(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    cookie = browser.get_cookie('token_22')
    print(cookie['value'])


def test_get_song_from_cookies(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3/index.html')
    cookies = browser.get_cookies()
    song = cookies[0]['name']
    time.sleep(2)
    browser.find_element(By.ID, 'phraseInput').send_keys(song)
    time.sleep(2)
    browser.find_element(By.ID, 'checkButton').click()
    time.sleep(2)
    print(browser.find_element(By.ID, 'result').text)


def test_delete_cookies(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3.2/index.html')
    browser.delete_all_cookies()
    time.sleep(10)


def test_add_cookies(browser):
    browser.get('https://parsinger.ru/selenium/6/6.3.3/index.html')
    cookie_dict = {
        'name': 'secretKey',    # Любое имя для cookie
        'value': 'selenium123',  # Любое значение для cookie
        # 'expiry': 2_000_000_000,      # Время жизни cookie в секундах
        # 'path': '/',                  # Директория на сервере дял которой будут доступны cookie
        # 'domain': 'parsinger.ru',     # Информация о домене и поддомене для которых доступны cookie
        # 'secure': True,   # or False - Сигнал браузера о том что передать cookie только по защищённому HTTPS
        # 'httpOnly': True,  # or False - Ограничивает доступ к cookie по средствам API
        # 'sameSite': 'Strict',  # or lax or none - Ограничение на передачу cookie между сайтами
    }
    browser.add_cookie(cookie_dict)
    browser.refresh()
    time.sleep(2)
    print(browser.find_element(By.ID, 'password').text)


def test_find_even_cookies(browser):
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    result = 0
    for cookie in cookies:
        cookie_name_number = cookie['name'].split('_')[-1]
        if cookie_name_number.isdigit() and int(cookie_name_number) % 2 == 0:
            result += int(cookie['value'])
    print(result)


def test_cookie_max_expiry(browser):
    browser.get('https://parsinger.ru/methods/5/index.html')
    links = browser.find_elements(By.CSS_SELECTOR, '.urls a')

    max_expiry = 0
    result = None

    for link in links:
        link.click()
        cookies = browser.get_cookies()

        for cookie in cookies:
            expiry = int(cookie['expiry'])
            if expiry > max_expiry:
                max_expiry = expiry
                result = browser.find_element(By.ID, 'result').text

        browser.back()

    print(result)


def test_get_secret_cookies(browser):
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    result = 0

    for cookie in cookies:
        if cookie['name'].startswith('secret_cookie_'):
            result += int(cookie['value'])

    print(result)


def test_find_youngest_developer(browser):
    browser.get('https://parsinger.ru/selenium/5.6/1/index.html')
    age = float('inf')
    cnt_skills = 0
    value = None

    for cookie in COOKIES:
        browser.add_cookie(cookie)
        browser.refresh()
        current_age = int(browser.find_element(By.ID, 'age').text[5:])
        current_cnt_skills = len(browser.find_elements(By.CSS_SELECTOR, '#skillsList > li'))
        if current_age < age and current_cnt_skills > cnt_skills:
            cnt_skills = current_cnt_skills
            age = current_age
            value = cookie['value']
        browser.delete_all_cookies()

    print(value)
