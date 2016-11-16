# cloudx5-benchmark
benchmark for cloudx5

## build cx5bench runtime image

    docker build -t cx5bench .

## create cx5bench container

    docker run -it --rm --name cx5bench cx5bench

## use cx5bench

    # config cx5bench
    # please use rancher account apikey
    cx5bench config
    
    # create envs
    cx5bench env-create 10
    
    # clean envs
    cx5bench env-clean
    
    # create 3 stacks with nginx-app
    cx5bench stack-create 3 -dp compose-test/nginx/docker-compose.yml -rp compose-test/nginx/rancher-compose.yml
    # create empty 3 stacks
    cx5bench stack-create 3
    # clean benchmark stacks
    cx5bench stack-clean
    
    #others please use
    cx5bench <command> --help
    
    


