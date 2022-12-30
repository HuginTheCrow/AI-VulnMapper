
# Use appropriate base image
FROM quantumcrack/vulnmapai-base:0.1 as base

# Copy scripts into the container
WORKDIR /app
COPY advising ./advising
COPY exploit ./exploit
COPY orchestration ./orchestration
COPY recon ./recon
COPY report ./report
COPY resources ./resources
COPY utils ./utils
COPY webapp ./webapp
COPY config.py .
COPY constants.py .