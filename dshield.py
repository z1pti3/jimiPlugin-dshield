import jimi

class _dshield(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        # Register models
        jimi.model.registerModel("dshieldBackscatter","_dshieldBackscatter","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldCloudIPs","_dshieldCloudIPs","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldCloudCidrs","_dshieldCloudCidrs","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldCurrentHandler","_dshieldCurrentHandler","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldInfoconLevel","_dshieldInfoconLevel","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldIntelfeed","_dshieldIntelfeed","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldIPInfo","_dshieldIPInfo","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldIPDetails","_dshieldIPDetails","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldPortInfo","_dshieldPortInfo","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldPortInfoByDate","_dshieldPortInfoByDate","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldTopPorts","_dshieldTopPorts","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldTopIPs","_dshieldTopIPs","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldAttackSources","_dshieldAttackSources","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldASNLookup","_dshieldASNLookup","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldDailySummary","_dshieldDailySummary","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldProject404Summary","_dshieldProject404Summary","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldProject404","_dshieldProject404","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldIPSurvivalTime","_dshieldIPSurvivalTime","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldThreatFeed","_dshieldThreatFeed","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldMSPatchDate","_dshieldMSPatchDate","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldGetMSPatch","_dshieldGetMSPatch","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldGetMSPatchCVEs","_dshieldGetMSPatchCVEs","_action","plugins.dshield.models.action")
        jimi.model.registerModel("dshieldGetMSPatchReplaces","_dshieldGetMSPatchReplaces","_action","plugins.dshield.models.action")
        return True

    def uninstall(self):
        # deregister models
        jimi.model.deregisterModel("dshieldBackscatter","_dshieldBackscatter","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldCloudIPs","_dshieldCloudIPs","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldCloudCidrs","_dshieldCloudCidrs","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldCurrentHandler","_dshieldCurrentHandler","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldInfoconLevel","_dshieldInfoconLevel","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldIntelfeed","_dshieldIntelfeed","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldIPInfo","_dshieldIPInfo","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldIPDetails","_dshieldIPDetails","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldPortInfo","_dshieldPortInfo","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldPortInfoByDate","_dshieldPortInfoByDate","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldTopPorts","_dshieldTopPorts","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldTopIPs","_dshieldTopIPs","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldAttackSources","_dshieldAttackSources","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldASNLookup","_dshieldASNLookup","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldDailySummary","_dshieldDailySummary","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldProject404Summary","_dshieldProject404Summary","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldProject404","_dshieldProject404","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldIPSurvivalTime","_dshieldIPSurvivalTime","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldThreatFeed","_dshieldThreatFeed","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldMSPatchDate","_dshieldMSPatchDate","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldGetMSPatch","_dshieldGetMSPatch","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldGetMSPatchCVEs","_dshieldGetMSPatchCVEs","_action","plugins.dshield.models.action")
        jimi.model.deregisterModel("dshieldGetMSPatchReplaces","_dshieldGetMSPatchReplaces","_action","plugins.dshield.models.action")
        return True

    def upgrade(self,LatestPluginVersion):
        pass
        #if self.version < 0.2:
