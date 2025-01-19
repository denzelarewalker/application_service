import logging
from aiokafka import AIOKafkaProducer
from .schemas import Application

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


KAFKA_TOPIC = "new_applications"


async def send_application(application: Application):
    producer = AIOKafkaProducer(bootstrap_servers="kafka:9092")
    await producer.start()
    try:
        await producer.send_and_wait(KAFKA_TOPIC, application.json().encode())
        logger.info(f"Successfully sent application to Kafka topic '{KAFKA_TOPIC}'")
    except Exception as e:
        logger.error(f"Failed to send application to Kafka: {e}")
    finally:
        await producer.stop()