FROM consul:1.15.4

COPY ./consul/config.json /consul/config/config.json

EXPOSE 8500
CMD ["agent", "-config-file=/consul/config/config.json"]
