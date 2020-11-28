#!/usr/bin/python
import jinja2
import os

OS = os.getenv('TM_SERV_OS')
ARCH = os.getenv('TM_SERV_ARCH')
URL_TRAEFIK = os.getenv('TM_URL_TRAEFIK')

def templating(folder, file):
  templateLoader = jinja2.FileSystemLoader(searchpath="./" + folder)
  templateEnv = jinja2.Environment(loader=templateLoader)
  template = templateEnv.get_template(file + ".j2")
  outputText = template.render(
    os=OS,
    arch=ARCH,
    url_traefik=URL_TRAEFIK
  )

  file = open("./" + folder + "/" + file, "w+")
  file.write(outputText)
  file.close()

templating("", "docker-compose.yml")
templating("authelia", "configuration.yml")