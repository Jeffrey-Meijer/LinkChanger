<?php
/**
 * @package ExposeElementor
 */
/*
 
Plugin Name: Expose Elementor REST API
Plugin URI: https://hq-online.nl
Description: Exposes the Elementor content to the REST API for further use
Version: 1.0
Author: HQ Online
Author URI: https://hq-online.nl/
License: GPLv2 or later
Text Domain: exposeelementor
*/


add_action("rest_api_init", "expose_elementor_content");

function expose_elementor_content() {
    register_rest_route(
        "hq/v1", "/elementor/footer",
        [
            "methods" => "GET",
            "callback" => function(\WP_REST_Request $req) {
                $contentElementor = "{}";
                $args = array (
                    "post_type" => "elementor_library",
                    "posts_per_page" => -1
                );

                if (class_exists("\\Elementor\\Plugin")) {
                    
                    $the_query = new WP_Query($args);
                    
                    if($the_query->have_posts()): 
                        while($the_query->have_posts()) : $the_query->the_post();
                            $post_meta = get_post_meta(get_the_ID());
                            if(in_array("footer",$post_meta["_elementor_template_type"])) {
                                $object = json_decode($post_meta["_elementor_data"][0], true);
                                $editors = array();

                                array_walk_recursive($object, function($v, $k) use (&$editors) {
                                  if ($k === 'editor' && strpos($v, 'webdesignhq') !== false && strpos($v, 'webdesignhq.nl') !== false) {
                                    $editors[] = $v;
                                  }
                                });

                                $editors = array_unique($editors);

                                return $editors;
                            }
                        endwhile;
                        wp_reset_query();
                    endif;

                }

                return $contentElementor;
            }
        ]
    );
    register_rest_route( # Add security
        "hq/v1", "/elementor/footer",
        [
            "methods" => "POST",
            "callback" => function(\WP_REST_Request $req) {
              $args = array(
                "post_type" => "elementor_library",
                "posts_per_page" => -1
              );
              if (class_exists("\\Elementor\\Plugin")) {
                  $parameters = $req->get_params();
                  // Check if JWT matches
                  $encoded_jwt = "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SjFjMlZ5Ym1GdFpTSTZJbWh4TFc5dWJHbHVaU0lzSW5CaGMzTWlPaUpVVlhRMFpFdG1VVlo2WmtKaGVERmFOR1owZFdSeWMzZ2lmUS5WYmZIbGF1bGh3RktybG9Zc0t0NFp1eGNFcEt6NGFiLU0zNTdKeGRUaXFr";
                  if (base64_encode($parameters["jwt_token"]) != $encoded_jwt) {
                      return '{"message": "Incorrect authentication supplied!"}';
                  } 

                  $the_query = new WP_Query($args);

                  if ($the_query->have_posts()) :
                      while ($the_query->have_posts()) : $the_query->the_post();
                          $post_meta = get_post_meta(get_the_ID());
                          if (in_array("footer", $post_meta["_elementor_template_type"])) {
                            $object = json_decode($post_meta["_elementor_data"][0], true);
                            $new_data = $parameters["footer"];
                              
                            array_walk_recursive($object, function(&$v, $k) use ($new_data) {
                              if ($k === 'editor' && strpos($v, 'webdesignhq') !== false && strpos($v, 'webdesignhq.nl') !== false) { # Now checks if the word "webdesignhq" and "webdesignhq.nl" is in the value.
                                $v = $new_data;
                              }
                            });

                            update_post_meta(get_the_ID(), "_elementor_data", addslashes(json_encode($object)));
                          }
                      endwhile;
                    wp_reset_query();
                endif;
              }
            }
        ]
    );
}

?>