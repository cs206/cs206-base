#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import util

from random import choice

class MainHandler(webapp.RequestHandler):
    def get(self):
        greetings = ["hola","sup","HEY","greetings","shalom"]
        greeting = choice(greetings)
        suits = ['clubs','hearts','spades','diamonds']
        card_name = "%s of %s" % (choice(range(1,11)),choice(suits))
       # self.response.out.write('<html><b>%s</b></html>' % card_name)
        #self.response.out.write('<html><b> %s world!</b></html>' % greetings)

        self.response.out.write(template.render("templates/index.html",{'card_name' : card_name,'greetings' : greeting}))

    def post(self):
         self.response.out.write("Submitted!")


def main():
    application = webapp.WSGIApplication([('/', MainHandler),
                                          ("/submit",MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
