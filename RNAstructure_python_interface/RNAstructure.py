# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_RNAstructure', [dirname(__file__)])
        except ImportError:
            import _RNAstructure
            return _RNAstructure
        if fp is not None:
            try:
                _mod = imp.load_module('_RNAstructure', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _RNAstructure = swig_import_helper()
    del swig_import_helper
else:
    import _RNAstructure
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class RNA(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RNA, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RNA, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNAstructure.new_RNA(*args)
        try: self.this.append(this)
        except: self.this = this
    def GetErrorCode(self): return _RNAstructure.RNA_GetErrorCode(self)
    def GetErrorMessage(self, *args): return _RNAstructure.RNA_GetErrorMessage(self, *args)
    def GetErrorMessageString(self, *args): return _RNAstructure.RNA_GetErrorMessageString(self, *args)
    def SpecifyPair(self, *args): return _RNAstructure.RNA_SpecifyPair(self, *args)
    def RemovePairs(self, structurenumber = 1): return _RNAstructure.RNA_RemovePairs(self, structurenumber)
    def RemoveBasePair(self, *args): return _RNAstructure.RNA_RemoveBasePair(self, *args)
    def CalculateFreeEnergy(self, structurenumber = 1, UseSimpleMBLoopRules = False): return _RNAstructure.RNA_CalculateFreeEnergy(self, structurenumber, UseSimpleMBLoopRules)
    def WriteThermodynamicDetails(self, *args): return _RNAstructure.RNA_WriteThermodynamicDetails(self, *args)
    def FoldSingleStrand(self, *args): return _RNAstructure.RNA_FoldSingleStrand(self, *args)
    def GenerateAllSuboptimalStructures(self, *args): return _RNAstructure.RNA_GenerateAllSuboptimalStructures(self, *args)
    def MaximizeExpectedAccuracy(self, *args): return _RNAstructure.RNA_MaximizeExpectedAccuracy(self, *args)
    def PartitionFunction(self, *args): return _RNAstructure.RNA_PartitionFunction(self, *args)
    def PredictProbablePairs(self, probability = 0): return _RNAstructure.RNA_PredictProbablePairs(self, probability)
    def ProbKnot(self, iterations = 1, MinHelixLength = 1): return _RNAstructure.RNA_ProbKnot(self, iterations, MinHelixLength)
    def ProbKnotFromSample(self, iterations = 1, MinHelixLength = 1): return _RNAstructure.RNA_ProbKnotFromSample(self, iterations, MinHelixLength)
    def ReFoldSingleStrand(self, *args): return _RNAstructure.RNA_ReFoldSingleStrand(self, *args)
    def Stochastic(self, *args): return _RNAstructure.RNA_Stochastic(self, *args)
    def ForceDoubleStranded(self, *args): return _RNAstructure.RNA_ForceDoubleStranded(self, *args)
    def ForceFMNCleavage(self, *args): return _RNAstructure.RNA_ForceFMNCleavage(self, *args)
    def ForceMaximumPairingDistance(self, *args): return _RNAstructure.RNA_ForceMaximumPairingDistance(self, *args)
    def ForceModification(self, *args): return _RNAstructure.RNA_ForceModification(self, *args)
    def ForcePair(self, *args): return _RNAstructure.RNA_ForcePair(self, *args)
    def ForceProhibitPair(self, *args): return _RNAstructure.RNA_ForceProhibitPair(self, *args)
    def ForceSingleStranded(self, *args): return _RNAstructure.RNA_ForceSingleStranded(self, *args)
    def GetForcedDoubleStranded(self, *args): return _RNAstructure.RNA_GetForcedDoubleStranded(self, *args)
    def GetForcedFMNCleavage(self, *args): return _RNAstructure.RNA_GetForcedFMNCleavage(self, *args)
    def GetForcedModification(self, *args): return _RNAstructure.RNA_GetForcedModification(self, *args)
    def GetForcedPair(self, *args): return _RNAstructure.RNA_GetForcedPair(self, *args)
    def GetForcedProhibitedPair(self, *args): return _RNAstructure.RNA_GetForcedProhibitedPair(self, *args)
    def GetForcedSingleStranded(self, *args): return _RNAstructure.RNA_GetForcedSingleStranded(self, *args)
    def GetMaximumPairingDistance(self): return _RNAstructure.RNA_GetMaximumPairingDistance(self)
    def GetNumberOfForcedDoubleStranded(self): return _RNAstructure.RNA_GetNumberOfForcedDoubleStranded(self)
    def GetNumberOfForcedFMNCleavages(self): return _RNAstructure.RNA_GetNumberOfForcedFMNCleavages(self)
    def GetNumberOfForcedModifications(self): return _RNAstructure.RNA_GetNumberOfForcedModifications(self)
    def GetNumberOfForcedPairs(self): return _RNAstructure.RNA_GetNumberOfForcedPairs(self)
    def GetNumberOfForcedProhibitedPairs(self): return _RNAstructure.RNA_GetNumberOfForcedProhibitedPairs(self)
    def GetNumberOfForcedSingleStranded(self): return _RNAstructure.RNA_GetNumberOfForcedSingleStranded(self)
    def ReadConstraints(self, *args): return _RNAstructure.RNA_ReadConstraints(self, *args)
    def ReadSHAPE(self, *args): return _RNAstructure.RNA_ReadSHAPE(self, *args)
    def ReadDSO(self, *args): return _RNAstructure.RNA_ReadDSO(self, *args)
    def ReadSSO(self, *args): return _RNAstructure.RNA_ReadSSO(self, *args)
    def ReadExperimentalPairBonus(self, *args): return _RNAstructure.RNA_ReadExperimentalPairBonus(self, *args)
    def RemoveConstraints(self): return _RNAstructure.RNA_RemoveConstraints(self)
    def SetExtrinsic(self, *args): return _RNAstructure.RNA_SetExtrinsic(self, *args)
    def WriteConstraints(self, *args): return _RNAstructure.RNA_WriteConstraints(self, *args)
    def AddComment(self, *args): return _RNAstructure.RNA_AddComment(self, *args)
    def WriteCt(self, *args): return _RNAstructure.RNA_WriteCt(self, *args)
    def WriteDotBracket(self, *args): return _RNAstructure.RNA_WriteDotBracket(self, *args)
    def BreakPseudoknot(self, minimum_energy = True, structurenumber = 0): return _RNAstructure.RNA_BreakPseudoknot(self, minimum_energy, structurenumber)
    def ContainsPseudoknot(self, *args): return _RNAstructure.RNA_ContainsPseudoknot(self, *args)
    def GetEnsembleEnergy(self): return _RNAstructure.RNA_GetEnsembleEnergy(self)
    def GetFreeEnergy(self, *args): return _RNAstructure.RNA_GetFreeEnergy(self, *args)
    def GetPair(self, *args): return _RNAstructure.RNA_GetPair(self, *args)
    def GetPairEnergy(self, *args): return _RNAstructure.RNA_GetPairEnergy(self, *args)
    def GetPairProbability(self, *args): return _RNAstructure.RNA_GetPairProbability(self, *args)
    def GetStructureNumber(self): return _RNAstructure.RNA_GetStructureNumber(self)
    def DetermineDrawingCoordinates(self, *args): return _RNAstructure.RNA_DetermineDrawingCoordinates(self, *args)
    def GetCommentString(self, structurenumber = 1): return _RNAstructure.RNA_GetCommentString(self, structurenumber)
    def GetNucleotideXCoordinate(self, *args): return _RNAstructure.RNA_GetNucleotideXCoordinate(self, *args)
    def GetNucleotideYCoordinate(self, *args): return _RNAstructure.RNA_GetNucleotideYCoordinate(self, *args)
    def GetLabelXCoordinate(self, *args): return _RNAstructure.RNA_GetLabelXCoordinate(self, *args)
    def GetLabelYCoordinate(self, *args): return _RNAstructure.RNA_GetLabelYCoordinate(self, *args)
    def GetNucleotide(self, *args): return _RNAstructure.RNA_GetNucleotide(self, *args)
    def GetSequenceLength(self): return _RNAstructure.RNA_GetSequenceLength(self)
    def GetBackboneType(self): return _RNAstructure.RNA_GetBackboneType(self)
    def GetStructure(self): return _RNAstructure.RNA_GetStructure(self)
    def SetProgress(self, *args): return _RNAstructure.RNA_SetProgress(self, *args)
    def StopProgress(self): return _RNAstructure.RNA_StopProgress(self)
    def GetProgress(self): return _RNAstructure.RNA_GetProgress(self)
    __swig_destroy__ = _RNAstructure.delete_RNA
    __del__ = lambda self : None;
RNA_swigregister = _RNAstructure.RNA_swigregister
RNA_swigregister(RNA)

class Dynalign_object(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Dynalign_object, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Dynalign_object, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNAstructure.new_Dynalign_object(*args)
        try: self.this.append(this)
        except: self.this = this
    def Dynalign(self, *args): return _RNAstructure.Dynalign_object_Dynalign(self, *args)
    def WriteAlignment(self, *args): return _RNAstructure.Dynalign_object_WriteAlignment(self, *args)
    def ForceAlignment(self, *args): return _RNAstructure.Dynalign_object_ForceAlignment(self, *args)
    def GetForcedAlignment(self, *args): return _RNAstructure.Dynalign_object_GetForcedAlignment(self, *args)
    def ReadAlignmentConstraints(self, *args): return _RNAstructure.Dynalign_object_ReadAlignmentConstraints(self, *args)
    def Templatefromct(self, *args): return _RNAstructure.Dynalign_object_Templatefromct(self, *args)
    def Templatefromdsv(self, *args): return _RNAstructure.Dynalign_object_Templatefromdsv(self, *args)
    def GetBestPairEnergy(self, *args): return _RNAstructure.Dynalign_object_GetBestPairEnergy(self, *args)
    def GetLowestEnergy(self): return _RNAstructure.Dynalign_object_GetLowestEnergy(self)
    def GetErrorMessage(self, *args): return _RNAstructure.Dynalign_object_GetErrorMessage(self, *args)
    def SetProgress(self, *args): return _RNAstructure.Dynalign_object_SetProgress(self, *args)
    def StopProgress(self): return _RNAstructure.Dynalign_object_StopProgress(self)
    __swig_destroy__ = _RNAstructure.delete_Dynalign_object
    __del__ = lambda self : None;
Dynalign_object_swigregister = _RNAstructure.Dynalign_object_swigregister
Dynalign_object_swigregister(Dynalign_object)

class Multilign_object(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Multilign_object, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Multilign_object, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNAstructure.new_Multilign_object(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNAstructure.delete_Multilign_object
    __del__ = lambda self : None;
    def CountBP(self, i = 0, j = 0, percent = 0.8): return _RNAstructure.Multilign_object_CountBP(self, i, j, percent)
    def ProgressiveMultilign(self, *args): return _RNAstructure.Multilign_object_ProgressiveMultilign(self, *args)
    def MultiTempMultilign(self): return _RNAstructure.Multilign_object_MultiTempMultilign(self)
    def WriteAlignment(self, allali = "all.ali"): return _RNAstructure.Multilign_object_WriteAlignment(self, allali)
    def GetErrorCode(self): return _RNAstructure.Multilign_object_GetErrorCode(self)
    def GetErrorMessage(self, *args): return _RNAstructure.Multilign_object_GetErrorMessage(self, *args)
    def SetMaxPairs(self, *args): return _RNAstructure.Multilign_object_SetMaxPairs(self, *args)
    def GetMaxPairs(self): return _RNAstructure.Multilign_object_GetMaxPairs(self)
    def AverageLength(self): return _RNAstructure.Multilign_object_AverageLength(self)
    def SetIterations(self, it = 2): return _RNAstructure.Multilign_object_SetIterations(self, it)
    def GetIterations(self): return _RNAstructure.Multilign_object_GetIterations(self)
    def SetMaxDsv(self, maxdsvchange = 1): return _RNAstructure.Multilign_object_SetMaxDsv(self, maxdsvchange)
    def GetMaxDsv(self): return _RNAstructure.Multilign_object_GetMaxDsv(self)
    def GetSequenceNumber(self): return _RNAstructure.Multilign_object_GetSequenceNumber(self)
    def SetIndexSeq(self, *args): return _RNAstructure.Multilign_object_SetIndexSeq(self, *args)
    def GetIndexSeq(self): return _RNAstructure.Multilign_object_GetIndexSeq(self)
    def Randomize(self): return _RNAstructure.Multilign_object_Randomize(self)
    def AddOneInput(self, *args): return _RNAstructure.Multilign_object_AddOneInput(self, *args)
    def RemoveOneInput(self, *args): return _RNAstructure.Multilign_object_RemoveOneInput(self, *args)
    def SetSHAPESlope(self, slope = 1.8): return _RNAstructure.Multilign_object_SetSHAPESlope(self, slope)
    def GetSHAPESlope(self): return _RNAstructure.Multilign_object_GetSHAPESlope(self)
    def SetSHAPEIntercept(self, *args): return _RNAstructure.Multilign_object_SetSHAPEIntercept(self, *args)
    def GetSHAPEIntercept(self): return _RNAstructure.Multilign_object_GetSHAPEIntercept(self)
    def SetTemperature(self, temp = 310.15): return _RNAstructure.Multilign_object_SetTemperature(self, temp)
    def GetTemperature(self): return _RNAstructure.Multilign_object_GetTemperature(self)
    def SetNucType(self, isrna = True): return _RNAstructure.Multilign_object_SetNucType(self, isrna)
    def GetNucType(self): return _RNAstructure.Multilign_object_GetNucType(self)
    def CleanupIntermediateFiles(self): return _RNAstructure.Multilign_object_CleanupIntermediateFiles(self)
    def SetProgress(self, Progress = None): return _RNAstructure.Multilign_object_SetProgress(self, Progress)
    def StopProgress(self): return _RNAstructure.Multilign_object_StopProgress(self)
    def GetProgress(self): return _RNAstructure.Multilign_object_GetProgress(self)
    def GetInputFilenames(self): return _RNAstructure.Multilign_object_GetInputFilenames(self)
    def GetPairs(self): return _RNAstructure.Multilign_object_GetPairs(self)
    def get_energies(self): return _RNAstructure.Multilign_object_get_energies(self)
    def get_dGIndex(self): return _RNAstructure.Multilign_object_get_dGIndex(self)
    def get_pair_alignments(self): return _RNAstructure.Multilign_object_get_pair_alignments(self)
Multilign_object_swigregister = _RNAstructure.Multilign_object_swigregister
Multilign_object_swigregister(Multilign_object)

class Oligowalk_object(RNA):
    __swig_setmethods__ = {}
    for _s in [RNA]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Oligowalk_object, name, value)
    __swig_getmethods__ = {}
    for _s in [RNA]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Oligowalk_object, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNAstructure.new_Oligowalk_object(*args)
        try: self.this.append(this)
        except: self.this = this
    def Oligowalk(self, *args): return _RNAstructure.Oligowalk_object_Oligowalk(self, *args)
    def GetBreakTargetDG(self, *args): return _RNAstructure.Oligowalk_object_GetBreakTargetDG(self, *args)
    def GetDuplexDG(self, *args): return _RNAstructure.Oligowalk_object_GetDuplexDG(self, *args)
    def GetOligoOligoDG(self, *args): return _RNAstructure.Oligowalk_object_GetOligoOligoDG(self, *args)
    def GetOligoSelfDG(self, *args): return _RNAstructure.Oligowalk_object_GetOligoSelfDG(self, *args)
    def GetOverallDG(self, *args): return _RNAstructure.Oligowalk_object_GetOverallDG(self, *args)
    def GetTm(self, *args): return _RNAstructure.Oligowalk_object_GetTm(self, *args)
    def WriteReport(self, *args): return _RNAstructure.Oligowalk_object_WriteReport(self, *args)
    def OligoScreen(self, *args): return _RNAstructure.Oligowalk_object_OligoScreen(self, *args)
    def GetErrorMessage(self, *args): return _RNAstructure.Oligowalk_object_GetErrorMessage(self, *args)
    __swig_destroy__ = _RNAstructure.delete_Oligowalk_object
    __del__ = lambda self : None;
Oligowalk_object_swigregister = _RNAstructure.Oligowalk_object_swigregister
Oligowalk_object_swigregister(Oligowalk_object)

class hairpin_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, hairpin_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, hairpin_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["probability"] = _RNAstructure.hairpin_t_probability_set
    __swig_getmethods__["probability"] = _RNAstructure.hairpin_t_probability_get
    if _newclass:probability = _swig_property(_RNAstructure.hairpin_t_probability_get, _RNAstructure.hairpin_t_probability_set)
    __swig_setmethods__["i"] = _RNAstructure.hairpin_t_i_set
    __swig_getmethods__["i"] = _RNAstructure.hairpin_t_i_get
    if _newclass:i = _swig_property(_RNAstructure.hairpin_t_i_get, _RNAstructure.hairpin_t_i_set)
    __swig_setmethods__["j"] = _RNAstructure.hairpin_t_j_set
    __swig_getmethods__["j"] = _RNAstructure.hairpin_t_j_get
    if _newclass:j = _swig_property(_RNAstructure.hairpin_t_j_get, _RNAstructure.hairpin_t_j_set)
    def __init__(self): 
        this = _RNAstructure.new_hairpin_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNAstructure.delete_hairpin_t
    __del__ = lambda self : None;
hairpin_t_swigregister = _RNAstructure.hairpin_t_swigregister
hairpin_t_swigregister(hairpin_t)

class internal_loop_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, internal_loop_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, internal_loop_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["probability"] = _RNAstructure.internal_loop_t_probability_set
    __swig_getmethods__["probability"] = _RNAstructure.internal_loop_t_probability_get
    if _newclass:probability = _swig_property(_RNAstructure.internal_loop_t_probability_get, _RNAstructure.internal_loop_t_probability_set)
    __swig_setmethods__["i"] = _RNAstructure.internal_loop_t_i_set
    __swig_getmethods__["i"] = _RNAstructure.internal_loop_t_i_get
    if _newclass:i = _swig_property(_RNAstructure.internal_loop_t_i_get, _RNAstructure.internal_loop_t_i_set)
    __swig_setmethods__["j"] = _RNAstructure.internal_loop_t_j_set
    __swig_getmethods__["j"] = _RNAstructure.internal_loop_t_j_get
    if _newclass:j = _swig_property(_RNAstructure.internal_loop_t_j_get, _RNAstructure.internal_loop_t_j_set)
    __swig_setmethods__["k"] = _RNAstructure.internal_loop_t_k_set
    __swig_getmethods__["k"] = _RNAstructure.internal_loop_t_k_get
    if _newclass:k = _swig_property(_RNAstructure.internal_loop_t_k_get, _RNAstructure.internal_loop_t_k_set)
    __swig_setmethods__["l"] = _RNAstructure.internal_loop_t_l_set
    __swig_getmethods__["l"] = _RNAstructure.internal_loop_t_l_get
    if _newclass:l = _swig_property(_RNAstructure.internal_loop_t_l_get, _RNAstructure.internal_loop_t_l_set)
    def __init__(self): 
        this = _RNAstructure.new_internal_loop_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNAstructure.delete_internal_loop_t
    __del__ = lambda self : None;
internal_loop_t_swigregister = _RNAstructure.internal_loop_t_swigregister
internal_loop_t_swigregister(internal_loop_t)

class multibranch_loop_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, multibranch_loop_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, multibranch_loop_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["probability"] = _RNAstructure.multibranch_loop_t_probability_set
    __swig_getmethods__["probability"] = _RNAstructure.multibranch_loop_t_probability_get
    if _newclass:probability = _swig_property(_RNAstructure.multibranch_loop_t_probability_get, _RNAstructure.multibranch_loop_t_probability_set)
    __swig_setmethods__["branches"] = _RNAstructure.multibranch_loop_t_branches_set
    __swig_getmethods__["branches"] = _RNAstructure.multibranch_loop_t_branches_get
    if _newclass:branches = _swig_property(_RNAstructure.multibranch_loop_t_branches_get, _RNAstructure.multibranch_loop_t_branches_set)
    def __init__(self): 
        this = _RNAstructure.new_multibranch_loop_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNAstructure.delete_multibranch_loop_t
    __del__ = lambda self : None;
multibranch_loop_t_swigregister = _RNAstructure.multibranch_loop_t_swigregister
multibranch_loop_t_swigregister(multibranch_loop_t)


def hairpin(*args):
  return _RNAstructure.hairpin(*args)
hairpin = _RNAstructure.hairpin

def internal_loop(*args):
  return _RNAstructure.internal_loop(*args)
internal_loop = _RNAstructure.internal_loop

def multibranch_loop(*args):
  return _RNAstructure.multibranch_loop(*args)
multibranch_loop = _RNAstructure.multibranch_loop

def add_branch(*args):
  return _RNAstructure.add_branch(*args)
add_branch = _RNAstructure.add_branch

def show_hairpins(*args):
  return _RNAstructure.show_hairpins(*args)
show_hairpins = _RNAstructure.show_hairpins

def show_internal_loops(*args):
  return _RNAstructure.show_internal_loops(*args)
show_internal_loops = _RNAstructure.show_internal_loops

def show_mbl(*args):
  return _RNAstructure.show_mbl(*args)
show_mbl = _RNAstructure.show_mbl
class mb_element(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mb_element, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mb_element, name)
    __repr__ = _swig_repr
    __swig_setmethods__["i"] = _RNAstructure.mb_element_i_set
    __swig_getmethods__["i"] = _RNAstructure.mb_element_i_get
    if _newclass:i = _swig_property(_RNAstructure.mb_element_i_get, _RNAstructure.mb_element_i_set)
    __swig_setmethods__["j"] = _RNAstructure.mb_element_j_set
    __swig_getmethods__["j"] = _RNAstructure.mb_element_j_get
    if _newclass:j = _swig_property(_RNAstructure.mb_element_j_get, _RNAstructure.mb_element_j_set)
    __swig_setmethods__["is_a_pair"] = _RNAstructure.mb_element_is_a_pair_set
    __swig_getmethods__["is_a_pair"] = _RNAstructure.mb_element_is_a_pair_get
    if _newclass:is_a_pair = _swig_property(_RNAstructure.mb_element_is_a_pair_get, _RNAstructure.mb_element_is_a_pair_set)
    def __init__(self, *args): 
        this = _RNAstructure.new_mb_element(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _RNAstructure.delete_mb_element
    __del__ = lambda self : None;
mb_element_swigregister = _RNAstructure.mb_element_swigregister
mb_element_swigregister(mb_element)

class ProbScan(RNA):
    __swig_setmethods__ = {}
    for _s in [RNA]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ProbScan, name, value)
    __swig_getmethods__ = {}
    for _s in [RNA]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, ProbScan, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _RNAstructure.new_ProbScan(*args)
        try: self.this.append(this)
        except: self.this = this
    def probability_of_individual_hairpin(self, *args): return _RNAstructure.ProbScan_probability_of_individual_hairpin(self, *args)
    def probability_of_all_hairpins(self, *args): return _RNAstructure.ProbScan_probability_of_all_hairpins(self, *args)
    def probability_of_internal_loop(self, *args): return _RNAstructure.ProbScan_probability_of_internal_loop(self, *args)
    def probability_of_all_internal_loops(self, *args): return _RNAstructure.ProbScan_probability_of_all_internal_loops(self, *args)
    def probability_of_multibranch_loop(self, *args): return _RNAstructure.ProbScan_probability_of_multibranch_loop(self, *args)
    __swig_destroy__ = _RNAstructure.delete_ProbScan
    __del__ = lambda self : None;
ProbScan_swigregister = _RNAstructure.ProbScan_swigregister
ProbScan_swigregister(ProbScan)


def show_mb_element_array(*args):
  return _RNAstructure.show_mb_element_array(*args)
show_mb_element_array = _RNAstructure.show_mb_element_array
# This file is compatible with both classic and new-style classes.


