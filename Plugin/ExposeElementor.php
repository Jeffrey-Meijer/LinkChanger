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
                    $post_id = $req->get_param("id");
                    
                    $pluginElementor = \Elementor\Plugin::instance();
                    $the_query = new WP_Query($args);
                    
                    if($the_query->have_posts()): 
                        while($the_query->have_posts()) : $the_query->the_post();
                            $post_meta = get_post_meta(get_the_ID());
                            if(in_array("footer",$post_meta["_elementor_template_type"])) {
                                return $post_meta;
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
                    $post_id = $req->get_param("id");
                    $parameters = $req->get_params();

                    $pluginElementor = \Elementor\Plugin::instance();
                    $the_query = new WP_Query($args);

                    if ($the_query->have_posts()) :
                        while ($the_query->have_posts()) : $the_query->the_post();
                            $post_meta = get_post_meta(get_the_ID());
                            if (in_array("footer", $post_meta["_elementor_template_type"])) {
                                $new_data = $parameters["_elementor_data"];
                                // update_post_meta(get_the_ID(), "_elementor_data", $new_data);
                                // return $new_data;
                                // return $post_id;
                            }
                        endwhile;
                        wp_reset_query();
                    endif;
                }
                // $id = $req->get_param("id");
                // $data = $req->get_param("data");
                // return $data;
            }
        ]
    );
}

?>