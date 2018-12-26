# birdr

Birdr is an app designed to help biologists monitor and mantain banding station data. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

These pieces of software are required to run the project in development:
* VirtualBox
* Android Studio

### Installing

A step by step series of examples that tell you how to get a development env running

Add forwarding from android emulator to vagrant box.

** 1. Add Android emualtor ports to forward to the guest box **

in `~/.ssh/config` add the following

```
Host 127.0.0.1
    RemoteForward 5037 127.0.0.1:5037
```

Or optionally, you can just always enter the vagrant machine by using
```
vagrant ssh -- -R 5037:localhost:5037
```

** 2. Build the machine **
`cd` into the project and enter:

```
vagrant up 
```

This will begin the initial build of the project. This may take 10-25 minutes depending on your latency, box ram, etc. 


We're working to make the install process a little less gnarly.

## Running the tests

Functional tests can be ran by using:

```
manage.py test --patterfn="f*.py"
```

## Deployment

Skip this for now.

## Built With
* [Django 2.0](https://www.djangoproject.com/) - Backend Framework
* [Nativescript Vue](https://nativescript-vue.org/) - Frontend utilities.

## Contributing

If for some reason you want to contribute, just message me via the power of the internet.

## Versioning

Standard API versioning is in place. We'll be on 1.0 for a while. 

## Authors

* **Rob Wise** - *Developer*
* **Kayla Bott** - *Product Manager*

And check out the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Inspired by birdrs
