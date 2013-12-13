django-govdelivery
==================

It currently provides a form handler that allows for subscription to an arbitrary number of topics. Forms that submit to it should look roughly like this:

```html
<formaction="/subscriptions/new" method="POST">

<input type="hidden" name="code" value="SOME_TOPIC_CODE">
<input type="hidden" name="code" value="ANOTHER_TOPIC_CODE">
<input type="email" name="email" >
<button>Sign up</button>
</form>
```

Depends on the govdelivery python wrapper being installed:
https://github.com/rosskarchner/govdelivery
