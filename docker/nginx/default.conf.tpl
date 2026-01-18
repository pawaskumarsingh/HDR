server {
    listen ${LISTEN_PORT};

    server_name 3.110.84.189;

    #while running on local
    #please comment above one
    #on local and uncomment below one

    #server_name localhost;

    location /static {
        alias /app/static;
    }

    location /media {
        alias /app/media/;
    }

    location / {
        proxy_pass http://${APP_HOST}:${APP_PORT};
        include    /etc/nginx/proxy_params;
    }
}
