# Fairness First: A Visual Analytic Approach to Exploring Fairness in Pre-Processing Permutations

PreFair is a visual analytics system designed to assist machine learning model builders in exploring the trade-offs between various pre-processing strategies

### Docker

Install and run web server:
```
docker build . -t web && docker run -p 3000:3000 web
```

Install and run api server:
```
cd api
docker build . -t api && docker run -p 14324:14324 api
```

