from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint

# Inicializar o ChromeDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)  

# Acessar a página de login do Instagram
driver.get('https://www.instagram.com/accounts/login/')

# Fazer login
try:
    username = driver.find_element(By.NAME, 'username')
    username.send_keys('your_username')

    password = driver.find_element(By.NAME, 'password')
    password.send_keys('yourpass')

    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    sleep(5)  
except Exception as e:
    print(f"Erro durante o login: {e}")

# Pular o popup de notificação
try:
    agora_nao = driver.find_element(By.XPATH, '//button[text()="Agora não"]')
    agora_nao.click()
except Exception as e:
    print(f"Erro ao clicar em 'Agora não': {e}")

hashtag_list = ['programming', 'python', 'setup', 'football', 'programmer', 'web', 'webdesign',
                'webdeveloper', 'game', 'gamer', 'rust', 'html', 'css', 'javascript', 'tecnologia']

novos_users_seguidos = []
seguindo = 0
likes = 0
comentarios = 0

for hashtag in hashtag_list:
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
    sleep(3)

    try:
        primeira_thumb = driver.find_element(By.XPATH, '//article//a')
        primeira_thumb.click()
        sleep(randint(3, 4))

        for _ in range(1, 6):
            usuario = driver.find_element(By.XPATH, '//header//a').text

            if usuario not in novos_users_seguidos:
                seguir_button = driver.find_element(By.XPATH, '//button[text()="Seguir"]')
                if seguir_button:
                    seguir_button.click()
                    novos_users_seguidos.append(usuario)
                    seguindo += 1

                    # Curtir a postagem
                    like_button = driver.find_element(By.XPATH, '//section/span/button')
                    like_button.click()
                    likes += 1
                    sleep(randint(3, 4))

                    # Comentar na postagem
                    comment_button = driver.find_element(By.XPATH, '//section/span[2]/button')
                    comment_button.click()
                    comment_box = driver.find_element(By.XPATH, '//textarea')

                    com = randint(1, 10)
                    if com < 6:
                        comment_box.send_keys('Nice!')
                    elif com > 5 and com < 9:
                        comment_box.send_keys('Muito boomm!')
                    elif com == 9:
                        comment_box.send_keys('Bom trabalho')
                    elif com == 10:
                        comment_box.send_keys('Soft!!')

                    comment_box.send_keys(Keys.ENTER)
                    comentarios += 1
                    sleep(randint(2, 4))

                    # Ir para a próxima postagem
                    driver.find_element(By.LINK_TEXT, 'Seguinte').click()
                    sleep(randint(2, 4))
                else:
                    driver.find_element(By.LINK_TEXT, 'Seguinte').click()
    except Exception as e:
        print(f"Erro: {e}")
        continue

print(f'Liked {likes} fotos.')
print(f'Comentários em {comentarios} fotos.')
print(f'Seguindo {seguindo} novas pessoas.')

driver.quit()
