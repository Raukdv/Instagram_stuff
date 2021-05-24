# Instagram_stuff
Proyecto que usa instagram's basic view api

Consideraciones a tener:
1) Usa requests para las peticiones, asi que por favor usa "pip install requests"
2) Debes tener una cuenta en facebook for developers y haber seguido todos los pasos para tener una App/Api de visualización basica de instagram. Tambien puedes guiarte en: https://developers.facebook.com/docs/instagram-basic-display-api/getting-started
3) La redirect_uri no admite urls que no tengan ssl activo o por lo menos localhost, si se va a integrar una toma desde el parametro redirect_uri para obtener el valor de acceso "?code=access_code" se debera usar una url que no de problemas.
4) En nuestra vista de Template, no se necesita gran cosa, solo usar la construccion de url ofrecida por https://developers.facebook.com/docs/instagram-basic-display-api/reference/oauth-authorize, en nuestras funciones (request y getting_user) ya que son peticiones get y post podemos usar comandos curls para ejecutarlas (Vease en la  guia de arriba Autorización Oauth o en Basic Started)
