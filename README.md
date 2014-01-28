django-govdelivery
==================

It currently provides a form handler that allows for subscription to an arbitrary number of topics. Forms that submit to it should look roughly like this:

```html
<form action="/subscriptions/new" method="POST" enctype="application/x-www-form-urlencoded">

<input type="hidden" name="code" value="SOME_TOPIC_CODE">
<input type="hidden" name="code" value="ANOTHER_TOPIC_CODE">
<input type="input" name="questionid_12345_free"/>
<input type="email" name="email" >
<button>Sign up</button>
</form>
```

Depends on the govdelivery python wrapper being installed:
https://github.com/rosskarchner/govdelivery
