# EventPublisher

A Java application for generating and publishing sample events to a Kafka/Redpanda topic.

## Quick Start

1. Compile:
   ```
   javac -cp "path/to/dependencies/*" EventPublisher.java
   ```

2. Run:
   ```
   java -cp ".:path/to/dependencies/*" EventPublisher <bootstrap-server> [-p <port>] [-t <topic>] [-n <number-of-events>]
   ```

## Usage Examples

```
java EventPublisher localhost
java EventPublisher localhost -p 9093 -t custom-topic -n 10
```

## Options

- `<bootstrap-server>`: Required. Kafka bootstrap server (without port)
- `-p <port>`: Optional. Port number (default: 9092)
- `-t <topic>`: Optional. Kafka topic (default: events)
- `-n <number-of-events>`: Optional. Number of events to publish (default: 5)

## Dependencies

- Kafka Clients
- Protobuf Java Util

Ensure these are in your classpath when compiling and running.

## Event Structure

Events include: Event ID, Source, Timestamp, Environment, Event Type, Value, String Value, Metadata, Severity, User ID, and Session ID.

For more details, check the `createEvent()` method in `EventPublisher.java`.

## to run

Use `example/streaming/docker-compose.yml` to start a Kafka/Redpanda cluster, create a topic called test1, and run the EventPublisher application.

```bash
pants run src/jvm/eventing/main/ai/cipherowl/publisher:: -- localhost -p 19092 -t test1 -n 5
```
