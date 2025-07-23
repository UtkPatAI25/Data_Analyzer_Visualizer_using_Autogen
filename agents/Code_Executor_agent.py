#https://microsoft.github.io/autogen/stable//reference/python/autogen_ext.code_executors.docker.html#autogen_ext.code_executors.docker.DockerCommandLineCodeExecutor

'''
Note: 
The DockerCommandLineCodeExecutor is a code executor that runs code in a Docker container.
It is designed to execute code blocks in a secure and isolated environment, 
which is useful for running untrusted code or code that requires specific dependencies.
The executor first saves each code block in a file in the working directory, 
and then executes the code file in the container. 
The executor executes the code blocks in the order they are received. 
Currently, the executor only supports Python and shell scripts. 
For Python code, use the language “python” for the code block. 
For shell scripts, use the language “bash”, “shell”, “sh”, “pwsh”, “powershell”, or “ps1” for the code block.
'''



from autogen_agentchat.agents import CodeExecutorAgent

def getCodeExecutorAgent(code_executor):

    code_executor_agent = CodeExecutorAgent(
        name='Python_Code_Executor',
        code_executor=code_executor
    )

    return code_executor_agent