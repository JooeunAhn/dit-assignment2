import requests as rq

host = "http://35.205.120.202:8080/"

def raise_for_status(res, name):
    try:
        res.raise_for_status()
        print("{} test passed".format(name))
    except:
        print("{} error occured".format(name))

def test_get_container_list():
    res = rq.get(host + "containers")
    raise_for_status(res, "get_container_list")

def test_get_running_container_list():
    res = rq.get(host + "containers?state=running")
    raise_for_status(res, "get_running_container_list")

def test_get_service_list():
    res = rq.get(host + "services")
    raise_for_status(res, "get_service_list")

def test_get_node_list():
    res = rq.get(host + "nodes")
    raise_for_status(res, "get_node_list")

def test_get_image_list():
    res = rq.get(host + "images")
    raise_for_status(res, "get_image_list")

def test_post_image():
    context = '{"file": "/home/d17123391/dit-assignment2"}'
    res = rq.post(host + "images", data=context)
    raise_for_status(res, "post_image_list")

def test_post_container():
    import json
    res = rq.get(host + "images")
    data = json.loads(res.text)

    if len(data):
        context = '{"image": "%s"}' % data[0].get('id')
        res = rq.post(host + "containers", data=context)

    raise_for_status(res, "post_container")

def test_patch_image():
    import json
    res = rq.get(host + "images")
    data = json.loads(res.text)

    if len(data):
        context = '{"tag": "test:1.0"}'
        res = rq.patch(host + "images/" + data[0].get('id'), data=context)
    
    raise_for_status(res, "patch_image")

def test_patch_container():
    import json
    res = rq.get(host + "containers")
    data = json.loads(res.text)

    if len(data):
        context = '{"status": "stopped"}'
        res = rq.patch(host + "containers/" + data[0].get('id'), data=context)

    raise_for_status(res, "patch_container")

def test_delete_image():
    import json
    res = rq.get(host + "images")
    data = json.loads(res.text)

    if len(data):
        res = rq.delete(host + "images/" + data[0].get('id'))

    raise_for_status(res, "delete_image")

def test_delete_container():
    import json
    res = rq.get(host + "containers")
    data = json.loads(res.text)

    if len(data):
        res = rq.delete(host + "containers/" + data[0].get('id'))

    raise_for_status(res, "delete_container")

def test_delete_images():
    res = rq.delete(host + "images")
    raise_for_status(res, "delete_images")

def test_delete_containers():
    res = rq.delete(host + 'containers')
    raise_for_status(res, "delete_containers")

if __name__ == "__main__":
    test_get_container_list()
    test_get_running_container_list()
    test_get_service_list()
    test_get_node_list()
    test_get_image_list()
    test_post_image()
    test_post_container()
    test_patch_image()
    test_patch_container()
    test_delete_container()
    test_delete_containers()
    test_delete_image()
    test_delete_images()

