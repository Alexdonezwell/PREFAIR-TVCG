# Fairness First: A Visual Analytic Approach to Exploring Fairness in Pre-Processing Permutations

PreFair is a visual analytics system designed to assist machine learning model builders in exploring the trade-offs between various pre-processing strategies. The system is packaged within a Docker container for easier installation and deployment. Currently, the Docker container does not support deployment on Mac M1/M2 chips: https://www.docker.com/blog/apple-silicon-m1-chips-and-docker/. Please install and deploy the PreFair system on the X86 CPU-based environment if you use the Docker container. For Mac M1/M2 users, please deploy the system on your local machine using npm package manager.

### Deploy with Docker

For computers that are not using Mac M1/M2 chips, please make sure the Docker container has been installed on your computer before running the following commands. You can install the Docker container from https://www.docker.com/get-started/.

Install and run web server:
```
docker build . -t web && docker run -p 3000:3000 web
```

Install and run the Python api server:
```
cd api
docker build . -t api && docker run -p 14324:14324 api
```


### Deploy with npm

For computers that are using Mac M1/M2 chips, please use npm package manager to deploy the PreFair system on your local machine. You can install node.js and npm from https://docs.npmjs.com/downloading-and-installing-node-js-and-npm. Please note that the dependent Python libraries are listed in the api/requirement.txt.

Install and run web server:
```
npm install
npm start
```

Install and run the Python api server:
```
cd api
pip install -r requirement.txt
python api.py
```
