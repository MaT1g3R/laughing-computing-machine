FROM rust:alpine as builder

WORKDIR /app

COPY Cargo.lock Cargo.toml /app
COPY src /app/src/

RUN cargo build --release

FROM scratch

WORKDIR /app
COPY --from=builder /app/target/release/laughing-computing-machine /app
ENTRYPOINT ["/app/laughing-computing-machine"]
