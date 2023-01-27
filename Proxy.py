import urllib.request
url = 'https://free-proxy-list.net/'
user_agent = "Mozilla/5.0 (WindowS; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/ 20091201 Firefox/3.5.6 GTB5"
try :
    req = urllib.request.Request(url)
    req.add_header("User-Agent", user_agent)
    sorce_code = urllib.request.urlopen(req)
    part = str(sorce_code.read())
    part= part.split ("<tbody> ")
    part = part[1].split("</tbody" )
    part = part[0].split("<tr><td>")
    porxies ='' 
    for proxy in part:
        proxy = proxy.split ("</td> <td> " )
        try:
            porxies = porxiestproxy[0]+":"+proxy[1]+'\n' 
        except:
            pass
    out_file.write(porxies)
    out_file.close()     
    print ("Proxiex download successfully" )
                                                                                               
except:
    print ("error")