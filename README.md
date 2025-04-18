
CDK deploys a producer bucket and a consumer lambda. Lambda knows about producer bucket.

# Create virtual env
To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Setting up the environment
Open up the env.sh file and modify, then source the file to set the environment.

```
$ source ./env.sh
```

## Useful commands

All CDK commands are available, this project uses a Makefile. See Makefile for details.

### Make commands

* `make install`    install dependencies
* `make list`       list dependencies
* `make format`     format source code
* `make lint`       lint source code
* `make synth`      emits the synthesized CloudFormation template
* `make deploy`     deploy this stack to your default AWS account/region
* `make destroy`    destroy this stack


### CDK commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

