import jimi
from plugins.dshield.includes import dshield

class _dshieldBackscatter(jimi.action._action):
    email = str()
    dateStr = str()
    rows = 10
    
    def run(self,data,persistentData,actionResult):
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})
        
        result, statusCode = dshield._dshield(self.email).backscatter(dateStr,self.rows)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldCloudIPs(jimi.action._action):
    email = str()
    
    def run(self,data,persistentData,actionResult):
        result, statusCode = dshield._dshield(self.email).cloudIPs()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldCloudCidrs(jimi.action._action):
    email = str()
    
    def run(self,data,persistentData,actionResult):        
        result, statusCode = dshield._dshield(self.email).cloudCidrs()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldCurrentHandler(jimi.action._action):
    email = str()
    
    def run(self,data,persistentData,actionResult):        
        result, statusCode = dshield._dshield(self.email).handler()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldInfoconLevel(jimi.action._action):
    email = str()
    
    def run(self,data,persistentData,actionResult):        
        result, statusCode = dshield._dshield(self.email).infoconLevel()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldIntelfeed(jimi.action._action):
    email = str()
    
    def run(self,data,persistentData,actionResult):        
        result, statusCode = dshield._dshield(self.email).intelfeed()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldIPInfo(jimi.action._action):
    email = str()
    ip = str()
    
    def run(self,data,persistentData,actionResult):        
        ip = jimi.helpers.evalString(self.ip,{"data" : data})

        result, statusCode = dshield._dshield(self.email).ipInfo(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldIPDetails(jimi.action._action):
    email = str()
    ip = str()
    
    def run(self,data,persistentData,actionResult):        
        ip = jimi.helpers.evalString(self.ip,{"data" : data})

        result, statusCode = dshield._dshield(self.email).ipDetails(ip)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldPortInfo(jimi.action._action):
    email = str()
    port = str()
    
    def run(self,data,persistentData,actionResult):        
        port = jimi.helpers.evalString(self.port,{"data" : data})

        result, statusCode = dshield._dshield(self.email).portInfo(port)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldPortInfoByDate(jimi.action._action):
    email = str()
    port = str()
    dateStr = str()
    
    def run(self,data,persistentData,actionResult):        
        port = jimi.helpers.evalString(self.port,{"data" : data})
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).portInfoByDate(port,dateStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldTopPorts(jimi.action._action):
    email = str()
    records = int()
    dateStr = str()
    
    def run(self,data,persistentData,actionResult):        
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).topPorts(self.records,dateStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldTopIPs(jimi.action._action):
    email = str()
    records = int()
    dateStr = str()
    
    def run(self,data,persistentData,actionResult):        
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).topIPs(self.records,dateStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 


class _dshieldAttackSources(jimi.action._action):
    email = str()
    records = int()
    dateStr = str()
    
    def run(self,data,persistentData,actionResult):        
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).attackSources(self.records,dateStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldASNLookup(jimi.action._action):
    email = str()
    rows = int()
    asn = str()
    
    def run(self,data,persistentData,actionResult):        
        asn = jimi.helpers.evalString(self.asn,{"data" : data})

        result, statusCode = dshield._dshield(self.email).asnLookup(asn,self.rows)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldDailySummary(jimi.action._action):
    email = str()
    startDate = str()
    endDate = str()
    
    def run(self,data,persistentData,actionResult):        
        startDate = jimi.helpers.evalString(self.startDate,{"data" : data})
        endDate = jimi.helpers.evalString(self.endDate,{"data" : data})

        result, statusCode = dshield._dshield(self.email).dailySummary(startDate,endDate)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldProject404Summary(jimi.action._action):
    email = str()
    startDate = str()
    endDate = str()
    
    def run(self,data,persistentData,actionResult):        
        startDate = jimi.helpers.evalString(self.startDate,{"data" : data})
        endDate = jimi.helpers.evalString(self.endDate,{"data" : data})

        result, statusCode = dshield._dshield(self.email).Project404Summary(startDate,endDate)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldProject404(jimi.action._action):
    email = str()
    dateStr = str()
    rows = int()
    
    def run(self,data,persistentData,actionResult):        
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).Project404(dateStr,self.rows)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldIPSurvivalTime(jimi.action._action):
    email = str()
    dateStr = str()
    
    def run(self,data,persistentData,actionResult):        
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).getSurvivalTime(dateStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldThreatFeed(jimi.action._action):
    email = str()
    
    def run(self,data,persistentData,actionResult):        

        result, statusCode = dshield._dshield(self.email).getThreatFeeds()

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldMSPatchDate(jimi.action._action):
    email = str()
    dateStr = str()
    
    def run(self,data,persistentData,actionResult):        
        dateStr = jimi.helpers.evalString(self.dateStr,{"data" : data})

        result, statusCode = dshield._dshield(self.email).getMSPatchDate(dateStr)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldGetMSPatch(jimi.action._action):
    email = str()
    msID = str()
    
    def run(self,data,persistentData,actionResult):        
        msID = jimi.helpers.evalString(self.msID,{"data" : data})

        result, statusCode = dshield._dshield(self.email).getMSPatch(msID)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldGetMSPatchCVEs(jimi.action._action):
    email = str()
    msID = str()
    
    def run(self,data,persistentData,actionResult):        
        msID = jimi.helpers.evalString(self.msID,{"data" : data})

        result, statusCode = dshield._dshield(self.email).getMSPatchCVEs(msID)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 

class _dshieldGetMSPatchReplaces(jimi.action._action):
    email = str()
    msID = str()
    
    def run(self,data,persistentData,actionResult):        
        msID = jimi.helpers.evalString(self.msID,{"data" : data})

        result, statusCode = dshield._dshield(self.email).getMSPatchReplaces(msID)

        if result:
            actionResult["result"] = True
            actionResult["rc"] = statusCode
            actionResult["api_result"] = result
        else:
            actionResult["result"] = False
            actionResult["rc"] = statusCode
            actionResult["msg"] = "Failed to get a valid response from dshield API"
        return actionResult 
