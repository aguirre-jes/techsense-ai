from diagrams import Cluster, Diagram
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.engagement import SimpleEmailServiceSes
from diagrams.aws.integration import Eventbridge
from diagrams.aws.ml import Bedrock


with Diagram("TechSense MVP AWS Flow", show=False, direction="LR", outformat="png"):
    scheduler = Eventbridge("Friday Trigger")

    with Cluster("Lambda Pipeline"):
        ingest = Lambda("Ingest")
        score = Lambda("Score")
        summarize = Lambda("Summarize")
        deliver = Lambda("Deliver")

    store = Dynamodb("Article Store")
    model = Bedrock("Claude Haiku")
    email = SimpleEmailServiceSes("SES")

    scheduler >> ingest >> store
    ingest >> score >> store
    score >> summarize >> model
    summarize >> deliver >> email
