FROM rjvishwa07/oorts:ubuntu-jammy-base

# Set noninteractive mode for Debian package configuration
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install required packages
RUN apt-get update && \
    apt-get install -y tzdata

# Set the timezone (e.g., UTC)
RUN ln -fs /usr/share/zoneinfo/UTC /etc/localtime

RUN apt-get clean && apt-get update && apt-get upgrade -y && apt-get install --no-install-recommends -y \
        apt-transport-https \
        apt-utils \
        ca-certificates \
        openssh-client \
        curl \
        iptables \
        git \
        nano \
        gnupg \
        software-properties-common \
        supervisor \
        wget && \
    rm -rf /var/lib/apt/list/*

# Install Helm
RUN curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null && \
    sudo apt-get install -y apt-transport-https && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main"| sudo tee /etc/apt/sources.list.d/helm-stable-debian.list && \
    sudo apt-get update && \
    sudo apt-get install -y helm

# Download and run the installation script
RUN wget https://raw.githubusercontent.com/DATAOORTS/gfalcon/main/installation.sh && \
    chmod +x installation.sh && \
    ./installation.sh

#ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
#CMD ["bash"]
# Add a simple command that finishes execution
CMD ["echo", "Working Singlotron!"]