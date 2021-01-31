import requests
import json
from pathlib import Path

class _dshield():
    url = "http://isc.sans.edu/api"
    
    def __init__(self, email, ca=None, requestTimeout=30):
        self.requestTimeout = requestTimeout
        self.headers = {
            'User-Agent': '{0}'.format(email)
        }
        if ca:
            self.ca = Path(ca)
        else:
            self.ca = None

    def apiCall(self,endpoint,methord="GET",data=None):
        kwargs={}
        kwargs["headers"] = self.headers
        kwargs["timeout"] = self.requestTimeout
        if self.ca:
            kwargs["verify"] = self.ca
        try:
            if methord == "GET":
                response = requests.get("{0}/{1}?json".format(self.url,endpoint), **kwargs)
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return 0, "Connection Timeout"
        if response.status_code == 200:
            return json.loads(response.text), response.status_code
        return response.text, response.status_code

    def backscatter(self,dateStr,rows):
        response, statusCode = self.apiCall("backscatter/{0}/{1}".format(dateStr,rows))
        return response, statusCode


    def cloudIPs(self):
        response, statusCode = self.apiCall("cloudips")
        return response, statusCode

    def cloudCidrs(self):
        response, statusCode = self.apiCall("cloudcidrs")
        return response, statusCode

    def handler(self):
        response, statusCode = self.apiCall("handler")
        return response, statusCode

    def infoconLevel(self):
        response, statusCode = self.apiCall("infocon")
        return response, statusCode

    def intelfeed(self):
        response, statusCode = self.apiCall("intelfeed")
        return response, statusCode

    def ipInfo(self,ip):
        response, statusCode = self.apiCall("ip/{0}".format(ip))
        return response, statusCode

    def ipDetails(self,ip):
        response, statusCode = self.apiCall("ipdetails/{0}".format(ip))
        return response, statusCode

    def portInfo(self,port):
        response, statusCode = self.apiCall("port/{0}".format(port))
        return response, statusCode

    def portInfoByDate(self,port,date):
        response, statusCode = self.apiCall("portdate/{0}/{1}".format(port,date))
        return response, statusCode

    def topPorts(self,records,date):
        response, statusCode = self.apiCall("topports/records/{0}/{1}".format(records,date))
        return response, statusCode

    def topIPs(self,records,date):
        response, statusCode = self.apiCall("topips/records/{0}/{1}".format(records,date))
        return response, statusCode

    def attackSources(self,records,date):
        response, statusCode = self.apiCall("sources/attacks/{0}/{1}".format(records,date))
        return response, statusCode

    def asnLookup(self,asn,rows):
        response, statusCode = self.apiCall("asnum/{0}/{1}".format(rows,asn))
        return response, statusCode

    def dailySummary(self,startDate,EndDate):
        response, statusCode = self.apiCall("dailysummary/{0}/{1}".format(startDate,EndDate))
        return response, statusCode

    def Project404Summary(self,startDate,EndDate):
        response, statusCode = self.apiCall("404summary/{0}/{1}".format(startDate,EndDate))
        return response, statusCode

    def Project404(self,dateStr,rows):
        response, statusCode = self.apiCall("404detail/{0}/{1}".format(dateStr,rows))
        return response, statusCode

    def getSurvivalTime(self,dateStr):
        response, statusCode = self.apiCall("survivaltime/{0}".format(dateStr))
        return response, statusCode

    def getThreatFeeds(self):
        response, statusCode = self.apiCall("threatfeeds")
        return response, statusCode

    def getMSPatchDate(self,dateStr):
        response, statusCode = self.apiCall("getmspatchdate/{0}".format(dateStr))
        return response, statusCode

    def getMSPatch(self,kb):
        response, statusCode = self.apiCall("getmspatch/{0}".format(kb))
        return response, statusCode

    def getMSPatchCVEs(self,kb):
        response, statusCode = self.apiCall("getmspatchcves/{0}".format(kb))
        return response, statusCode

    def getMSPatchReplaces(self,kb):
        response, statusCode = self.apiCall("getmspatchreplaces/{0}".format(kb))
        return response, statusCode
