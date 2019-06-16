GET movies/movie/_search
{
  "query":{
    "match": {
      "title": "stranger things"
    }
  }
}
  
GET ratings/rating/_search

GET tags/tag/_search

GET _cat/indices

GET /ratings/rating/_search
{
  "size": 0, 
  "aggs":{
    "ratings":{
      "terms":{
        "field": "rating"
      }
    }
  }
}

GET ratings/rating/_search
{
  "size":0,
  "query":{
    "match":{
      "rating":5.0
    }
  },
  "aggs":{
    "ratings2":{
      "terms":{
        "field": "rating"
      }
    }
  }
}

GET ratings/rating/_search
{
  "size":0,
  "query": {
    "match_phrase": {
      "title": "Star Wars Episode IV"
    }
  },
  "aggs":{
    "avg_rating":{
      "avg":{
        "field":"rating"
      }
    }
  }
  
}

GET ratings/rating/_search
{
  "size":0,
  "aggs":{
    "whole_ratings":{
      "histogram": {
        "field": "rating",
        "interval": 1.0
      }
    }
  }
}

GET movies/movie/_search
{
  "size":0,
  "aggs":{
    "release":{
      "histogram": {
        "field": "year",
        "interval": 10
      }
    }
  }
}

GET logstash-2015.12.04/_search
{
  "size":0,
  "aggs": {
    "timestamp": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "hour"
      }
    }
  }
}

GET logstash-2015.12.04/_search
{
  "size":0,
  "query":{
      "match":{
        "agent":"Googlebot"
      }
  },
  "aggs": {
    "timestamp": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "hour"
      }
    }
  }
}

GET logstash-2015.12.04/_search
{
  "size":0,
  "query":{
      "match":{
        "response":"500"
      }
  },
  "aggs": {
    "timestamp": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "minute"
      }
    }
  }
}


GET ratings/rating/_search
{
  "size":0,
  "query":{
    "match_phrase": {
      "title": "Star Wars"
    }
  },
  "aggs": {
    "titles": {
      "terms": {
        "field": "title"
      },
      "aggs": {
        "avg_rating": {
          "avg": {
            "field":"rating"
          }
        }
      }
    }
  }
}

GET ratings/_mapping/rating
{
    "properties":{
      "title":{
        "type":"text",
        "fielddata":true
      }
    }
}

#did not work, so reindex

DELETE ratings


PUT ratings
{
  "mappings": {
    "rating":{
      "properties":{
        "title":{
          "type":"text",
          "fielddata":true,
          "fields":{
            "raw":{
              "type":"keyword"
            }
          }
        }
      }
    }
  }
}

GET ratings/_mapping


GET ratings/rating/_search
{
  "size":0,
  "query":{
    "match_phrase": {
      "title": "Star Wars"
    }
  },
  "aggs": {
    "titles": {
      "terms": {
        "field": "title.raw"
      },
      "aggs": {
        "avg_rating": {
          "avg": {
            "field":"rating"
          }
        }
      }
    }
  }
}