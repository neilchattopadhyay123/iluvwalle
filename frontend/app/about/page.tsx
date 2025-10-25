import { Navigation } from "@/components/navigation"
import { Footer } from "@/components/Footer"
import { Card, CardContent } from "@/components/ui/card"
import { Recycle, Target, Heart, Lightbulb } from "lucide-react"

export default function AboutPage() {
  return (
    <div className="min-h-screen">
      <Navigation />

      {/* Hero Section */}
      <section className="py-20 lg:py-32 bg-gradient-to-br from-primary/30 via-accent/20 to-secondary/30 relative overflow-hidden">
        <div className="absolute inset-0 opacity-20">
          <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(255,255,255,0.1),transparent_50%)]" />
        </div>
        <div className="relative container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl mx-auto text-center">
            <h1 className="text-4xl sm:text-5xl font-bold mb-6 text-balance">
              Our Directive: <span className="text-primary">Restore Earth</span>
            </h1>
            <p className="text-lg text-foreground/80 leading-relaxed">
              For 700 years, one small robot showed us that even the loneliest task can have the greatest purpose. We're
              here to help everyone become a part of Earth's restoration.
            </p>
          </div>
        </div>
      </section>

      {/* Story Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="text-3xl font-bold mb-6">The Mission Continues</h2>
              <div className="space-y-4 text-muted-foreground leading-relaxed">
                <p>
                  Earth didn't become covered in waste overnight. It happened one discarded item at a time, one confused
                  sorting decision at a time. But restoration works the same way—one correct choice at a time.
                </p>
                <p>
                  We built this system because sorting shouldn't be a mystery. When you know exactly where something
                  belongs, you're not just disposing of trash—you're giving materials a chance at a new life.
                </p>
                <p>
                  Our AI identifies materials instantly and provides clear guidance. No more guessing. No more
                  contamination. Just simple, effective recycling that actually makes a difference.
                </p>
              </div>
            </div>
            <div className="relative">
              <div className="aspect-square rounded-2xl bg-gradient-to-br from-secondary/20 to-accent/20 flex items-center justify-center">
                <img
                  src="/person-sorting-recyclables-correctly.jpg"
                  alt="Recycling process"
                  className="rounded-2xl object-cover w-full h-full"
                />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Values Section */}
      <section className="py-20 bg-muted/30">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl sm:text-4xl font-bold mb-4">Our Core Directives</h2>
            <p className="text-lg text-muted-foreground max-w-2xl mx-auto">The principles that guide our mission</p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <Card className="bg-card">
              <CardContent className="pt-6">
                <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center mb-4">
                  <Recycle className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Persistence</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  Like WALL-E, we never give up. Every item matters, every day counts.
                </p>
              </CardContent>
            </Card>

            <Card className="bg-card">
              <CardContent className="pt-6">
                <div className="h-12 w-12 rounded-lg bg-secondary/10 flex items-center justify-center mb-4">
                  <Target className="h-6 w-6 text-secondary" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Precision</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  Accurate sorting is everything. Our AI ensures you get it right every time.
                </p>
              </CardContent>
            </Card>

            <Card className="bg-card">
              <CardContent className="pt-6">
                <div className="h-12 w-12 rounded-lg bg-accent/10 flex items-center justify-center mb-4">
                  <Heart className="h-6 w-6 text-accent" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Care</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  We care about Earth and making restoration accessible to everyone.
                </p>
              </CardContent>
            </Card>

            <Card className="bg-card">
              <CardContent className="pt-6">
                <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center mb-4">
                  <Lightbulb className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Hope</h3>
                <p className="text-muted-foreground text-sm leading-relaxed">
                  Small actions lead to big changes. Together, we can restore our planet.
                </p>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* Impact Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl mx-auto">
            <h2 className="text-3xl font-bold mb-6 text-center">Mission Progress</h2>
            <div className="space-y-6">
              <Card className="border-l-4 border-l-primary bg-card">
                <CardContent className="pt-6">
                  <h3 className="text-xl font-semibold mb-2">Reducing Waste</h3>
                  <p className="text-muted-foreground leading-relaxed">
                    By helping users sort correctly, we've prevented thousands of recyclable items from ending up in
                    landfills.
                  </p>
                </CardContent>
              </Card>

              <Card className="border-l-4 border-l-secondary bg-card">
                <CardContent className="pt-6">
                  <h3 className="text-xl font-semibold mb-2">Growing Community</h3>
                  <p className="text-muted-foreground leading-relaxed">
                    More people join the mission every day. Together, we're proving that small bots—and small
                    actions—can change the world.
                  </p>
                </CardContent>
              </Card>

              <Card className="border-l-4 border-l-accent bg-card">
                <CardContent className="pt-6">
                  <h3 className="text-xl font-semibold mb-2">Restoring Hope</h3>
                  <p className="text-muted-foreground leading-relaxed">
                    Every correctly sorted item is a step toward a cleaner Earth. The directive continues, and we're
                    making progress.
                  </p>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <Footer />
    </div>
  )
}
