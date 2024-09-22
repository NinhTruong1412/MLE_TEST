-include env.sh
export

run-update_requirements:
	@python requirements > requirements.txt

run-app:
	@uvicorn app.main:app --reload

# build local image and run on local machine
test-serving-image: 
	@docker build -t $(IMAGE_NAME):$(IMAGE_VERSION) . && \
	docker tag $(IMAGE_NAME):$(IMAGE_VERSION) ai-projects/$(IMAGE_NAME):$(IMAGE_VERSION) && \
	docker run -p 80:8080 -e AIP_HTTP_PORT=8080 ai-projects/$(IMAGE_NAME):$(IMAGE_VERSION)