
from states import FeatureDesignGenerationState

GENERATION='generation'
REVIEWER = "reviewer"
BUCKETS = 'buckets'
RANK="rank"
DESCRIPTION = 'description'

COMBINED = 'combined'
CODE = 'code'

from langgraph.graph import END, START, StateGraph

from featureGenerationRunner import FeatureGenerationNode
from FeatureReviewRunner import FeatureReviewerNode
from FeatureBucketRunner import FeatureBucketNode


from FeatureRankProcess import FeatureRankNode
from WebDescriptionRunner import WebDescNode
from CombinedCodeRunner import CombinedCodeNode 

from CombinedFeatureRunner import CombinedFeatureNode 

graph = StateGraph(FeatureDesignGenerationState)
graph.set_entry_point(GENERATION)
graph.add_node(GENERATION,FeatureGenerationNode)
graph.add_node(REVIEWER,FeatureReviewerNode)
graph.add_node(BUCKETS,FeatureBucketNode)
graph.add_node(RANK,FeatureRankNode)
graph.add_node(DESCRIPTION,WebDescNode)
graph.add_node(COMBINED,CombinedFeatureNode)
graph.add_node(CODE,CombinedCodeNode)
graph.add_edge(GENERATION,REVIEWER)
graph.add_edge(REVIEWER,BUCKETS)
graph.add_edge(BUCKETS,RANK)

graph.add_edge(RANK,DESCRIPTION)
graph.add_edge(DESCRIPTION,COMBINED)
graph.add_edge(COMBINED,CODE)

graph.add_edge(CODE,END)


graph_compiled = graph.compile()

# data = graph_compiled.invoke({'UserInterest':'User is interested in gossip'})
# print(data)
