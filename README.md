# Fairness First: A Visual Analytic Approach to Exploring Fairness in Pre-Processing Permutations

PreFair is a visual analytics system designed to assist machine learning model builders in exploring the trade-offs between various pre-processing strategies. The system is packaged within a Docker container for easier installation and deployment. Currently, the Docker container does not support deployment on Mac M1/M2 chips: https://www.docker.com/blog/apple-silicon-m1-chips-and-docker/. Please install and deploy the PreFair system on the X86 CPU-based environment instead.

### Docker

Please make sure the Docker container has been installed on your computer before running the following commands. You can install the Docker container from https://www.docker.com/get-started/.

Install and run web server:
```
docker build . -t web && docker run -p 3000:3000 web
```

Install and run api server:
```
cd api
docker build . -t api && docker run -p 14324:14324 api
```


###
