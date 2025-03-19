from CombinedCode import CombinedCodeProcess 

from states import FeatureDesignGenerationState

def CombinedCodeNode(state:FeatureDesignGenerationState):
    print("Enetered Combined script feature Node")
    userInterest = state['UserInterest']
    FeatureGenerated = state['FeaturesGenerated']
    
    FeatureReview = state['FeatureReview']
    FeatureBucket = state['FeaturesBucketed']
    FeatureRanks = state['FeaturesRanked']
    WebDescriptions = state['WebsiteDescriptions']
    CombinedFeature = state['CombinedFeatureDescription']
    CombinedCode = CombinedCodeProcess.invoke({'Featuredescription':CombinedFeature})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated,'FeatureReview':FeatureReview,'FeaturesBucketed':FeatureBucket,"FeaturesRanked":FeatureRanks,"WebsiteDescriptions":WebDescriptions,"CombinedFeatureDescription":CombinedFeature,"Code":CombinedCode}