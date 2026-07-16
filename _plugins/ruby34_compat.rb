# Compatibility for Liquid 4.0.3, which is pinned by github-pages 227.
# Ruby 3.2 deprecated and Ruby 3.4 removed the legacy object taint API.
if RUBY_VERSION >= "3.4"
  class Object
    def tainted?
      false
    end

    def untaint
      self
    end
  end
end
