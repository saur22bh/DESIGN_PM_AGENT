from featureGeneration import FeatureGenerationProcess
from states import FeatureDesignGenerationState

def FeatureGenerationNode(state:FeatureDesignGenerationState):
    print("Enetered Feature Generation Node")
    userInterest = state['UserInterest']
    FeatureGenerated = FeatureGenerationProcess.invoke({'user_interests':userInterest})
    return {'UserInterest':userInterest,'FeaturesGenerated':FeatureGenerated}