# HW-1 Answers

## 1.Explain the order of the instructions in your Dockerfile. What would happen to build time if you changed the order of two of them?

I copied `requirements.txt` and installed the dependencies before copying the application source code. This order allows Docker to reuse the dependency installation layer when only the application code changes. If I copied all source files first, a code change could invalidate the cache and cause the dependencies to be installed again. Keeping dependencies separate makes rebuilds faster.

## 2. What happens to data written inside a container when the container is removed? How would you keep the data, and where should an application keep important state?

Data written only inside a container's writable filesystem can be lost when the container is removed. A Docker volume keeps data separately from the container, so a new container can reuse the same data. In this project, I mounted a named volume at `/data` and verified that the visit counter survived container removal. Important application state should be stored in persistent storage, such as a Docker volume or a suitable database.

## 3. Why is the latest tag a risk for reproducibility? What did you use instead?

The `latest` tag can point to a different image over time, so rebuilding the same Dockerfile may produce a different environment. This makes builds less predictable and can introduce unexpected changes. I used the `python:3.12-slim` image pinned to its SHA-256 digest instead. This identifies the specific base image used for the build.

## 4. Image Size

The `ceng413-hw1:v1` image has a content size of 48.9 MB and a disk usage of 200 MB. The base image `python:3.12-slim` has a content size of 45.4 MB and a disk usage of 179 MB.

## AI assistance disclosure

I used ChatGPT to understand Docker concepts, troubleshoot errors, and review my implementation and tests. I ran the commands and tests myself and checked the results.