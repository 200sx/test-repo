from aws_cdk import core as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
import aws_cdk.aws_codepipeline_actions
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class TestRepoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                    pipeline_name="Test_pipeline",
                    synth=ShellStep("Synth", 
                        input=CodePipelineSource.git_hub(repo_string="200sx/test-repo",
                        branch="master",
                        authentication=cdk.SecretValue.secrets_manager('githubtok'),
                        trigger=aws_cdk.aws_codepipeline_actions.GitHubTrigger.POLL),
                        commands=["npm install -g aws-cdk", 
                            "python -m pip install -r requirements.txt", 
                            "cdk synth"]
                    )
                )