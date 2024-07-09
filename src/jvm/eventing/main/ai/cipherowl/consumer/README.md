# EventConsumer

Sample Java application for consuming events from Kafka/Redpanda topics.

## Quick Start

1. Compile:
   ```
   pants package src/jvm/eventing/main/ai/cipherowl/consumer::
   ```

2. Run:
   ```
   pants run src/jvm/eventing/main/ai/cipherowl/consumer:: -- <bootstrap-server> [-p <port>] [-t <topic>] [-g <group-id>]
   ```

## Usage Example

```
java EventConsumer localhost -p 19092 -t test1 -g my-consumer-group
```

## Options

- `<bootstrap-server>`: Required. Kafka bootstrap server (without port)
- `-p <port>`: Optional. Port number (default: 9092)
- `-t <topic>`: Optional. Kafka topic (default: events)
- `-g <group-id>`: Optional. Consumer group ID (default: event-consumer-group)

## Dependencies

- Kafka Clients
- Protobuf Java Util
- EventDOTProto.java (from our Protobuf definitions)

Ensure these are in your classpath when compiling and running.

## Notes

- Consumes events published by our EventPublisher
- Prints event details to console
- Modify `processEvent()` method to customize event handling

## To Run

Use `example/streaming/docker-compose.yml` to start a Kafka/Redpanda cluster, then run:

```bash
pants run src/jvm/eventing/main/ai/cipherowl/consumer:: -- localhost -p 19092 -t test1 -g my-consumer-group
```