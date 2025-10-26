import { Navigation } from "@/components/navigation"
import { Footer } from "@/components/Footer"
import { Card, CardContent } from "@/components/ui/card"
import { Recycle, Target, Heart, Lightbulb } from "lucide-react"
import Image from 'next/image';

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
              Our Mission: <span className="text-primary">Restore Earth</span>
            </h1>
            <p className="text-lg text-foreground/80 leading-relaxed">
              For 700 years, one small robot showed us that even the loneliest task can have the greatest purpose. We're
              here to help everyone become a part of Earth's restoration.
            </p>
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

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
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
                  Accurate sorting is everything. Our AI ensures you get it right.
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
          </div>
        </div>
      </section>

      {/* Team Section */}
      <section className="py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-3xl mx-auto text-center">
            <h2 className="text-3xl sm:text-4xl font-bold mb-4">Our Team</h2>
            <div className="space-y-6 py-6">
              <Image src="snacks.jpg" alt="Our HackPSU team" width={720} height={540} />
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <Footer />
    </div>
  )
}
